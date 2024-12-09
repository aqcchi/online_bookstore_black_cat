from django.core.exceptions import ValidationError
from django.test import TestCase
from common.validators import no_profanity_validator


class TestProfanityValidator(TestCase):

    def test__no_profanity_validator__valid_comment(self):
        # testing valid comment not containing profanity
        valid_comment = "A very good book!"
        try:
            no_profanity_validator(valid_comment)
        except ValidationError:
            self.fail("ValidationError raised unexpectedly for a valid comment.")

    def test__no_profanity_validator__invalid_comment(self):
        # testing invalid comment containing profanity
        invalid_comment = "You are a jerk!"

        # actual profanity detection from better_profanity
        with self.assertRaises(ValidationError):
            no_profanity_validator(invalid_comment)
