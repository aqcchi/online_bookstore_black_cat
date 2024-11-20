from django.db import models
from authors.validators import NameValidator


class Author(models.Model):

    first_name = models.CharField(
        max_length=50,
        validators=[
            NameValidator(message="First name must contain only letters, spaces, and hyphens."),
        ]
    )

    last_name = models.CharField(
        max_length=50,
        validators=[
            NameValidator(message="Last name must contain only letters, spaces, and hyphens."),
        ]
    )

    picture = models.URLField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
