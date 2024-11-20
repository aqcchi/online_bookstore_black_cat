from django.db import models


class Book(models.Model):

    title = models.CharField(max_length=100)

    authors = models.ManyToManyField(
        to='authors.Author',
        blank=True,
        related_name='books',
    )

    description = models.TextField(default=None)

    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    book_available = models.BooleanField(default=False)

    # number_of_copies = models.PositiveIntegerField()

    # condition_choices = [
    #     ('new', 'New'),
    #     ('used', 'Used'),
    #     ('damaged', 'Damaged'),
    # ]
    #
    # condition = models.CharField(max_length=10, choices=condition_choices)

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
