from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
from common.validators import no_profanity_validator


class Profile(models.Model):

    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name='profile',
        )

    bio = models.TextField(
        null=True,
        blank=True,
        validators=[
            MaxLengthValidator(500, message="Bio cannot be longer than 500 characters."),
            no_profanity_validator,
        ],
    )

    profile_picture = models.URLField(
        null=True,
        blank=True
    )

    email = models.EmailField()

    def __str__(self):
        return f"{self.user.username}'s profile"
