from better_profanity import profanity
from django.core.exceptions import ValidationError


def no_profanity_validator(value):
    if profanity.contains_profanity(value):
        raise ValidationError("Comment contains inappropriate language.")