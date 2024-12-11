from django.contrib.auth.models import User
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

    ordered_book = models.ForeignKey(
        to='books.Book',
        max_length=100,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        to=User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    amount_paid = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
    )

    is_completed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.ordered_book:
            self.amount_paid = self.ordered_book.price or 0  # if price is None
        else:
            self.amount_paid = 0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.id}"

