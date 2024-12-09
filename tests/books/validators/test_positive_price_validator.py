from django.core.exceptions import ValidationError
from django.test import TestCase
from books.validators import validate_positive_price


class TestPositivePriceValidator(TestCase):

    def setUp(self):
        self.validator = validate_positive_price

    def test__valid_price__expect_no_errors(self):
        try:
            self.validator(10.00)
        except ValidationError:
            self.fail('validate_positive_price raised ValidationError for a valid price')

    def test__zero_price__expect_validation_error(self):
        with self.assertRaises(ValidationError) as ve:
            self.validator(0)

        self.assertEqual(str(ve.exception), "['Price must be a positive number.']")

    def test__negative_price__expect_validation_error(self):
        with self.assertRaises(ValidationError) as ve:
            self.validator(-5.00)

        self.assertEqual(str(ve.exception), "['Price must be a positive number.']")
