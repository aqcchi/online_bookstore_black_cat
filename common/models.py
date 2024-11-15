from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Comment(models.Model):

    to_book = models.ForeignKey(
        to='books.Book',
        on_delete=models.CASCADE,
        related_name='comments',
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:50]

    class Meta:
        ordering = ['created_at',]
