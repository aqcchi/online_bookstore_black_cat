from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.utils.deconstruct import deconstructible


@deconstructible
class NameValidator:
    def __init__(self, message=None):
        if message is None:
            self.message = "The name should only contain alphabetic characters, spaces, or hyphens."
        else:
            self.message = message

    def __call__(self, value):
        if slugify(value) != value.lower():
            raise ValidationError(self.message)