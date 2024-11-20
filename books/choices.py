from django.db import models


class BookConditionChoices(models.TextChoices):
    NEW = 'New', 'New'
    USED = 'Used', 'Used'
    DAMAGED = 'Damaged', 'Damaged'