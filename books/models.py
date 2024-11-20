from django.db import models
from books.choices import BookConditionChoices
from books.validators import validate_positive_price


class Book(models.Model):

    title = models.CharField(max_length=100)

    authors = models.ManyToManyField(
        to='authors.Author',
        blank=True,
        related_name='books',
    )

    description = models.TextField(
        default=None,
        null=True,
        blank=True,
    )

    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[validate_positive_price]
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    book_available = models.BooleanField(default=False)

    condition = models.CharField(
        max_length=10,
        choices=BookConditionChoices.choices,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title


class Order(models.Model):

    product = models.ForeignKey(
        to='books.Book',
        max_length=100,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title if self.product else "No Product"
