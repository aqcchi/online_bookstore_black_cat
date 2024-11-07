from django.db import models


class Author(models.Model):

    first_name = models.CharField(
        max_length=50,
    )

    last_name = models.CharField(
        max_length=50,
    )

    picture = models.URLField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    books = models.ManyToManyField(
        to='books.Book',
        blank=True,
        related_name='authors',
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
