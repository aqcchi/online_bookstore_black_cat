from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance: UserModel, created: bool, **kwargs):
    if created:
        Profile.objects.create(user=instance, email=instance.email)


@receiver(post_save, sender=UserModel)  # optional but good in case of updates
def save_user_profile(sender, instance: UserModel, **kwargs):
    instance.profile.save()


@receiver(post_delete, sender=Profile)
def delete_user_when_profile_deleted(sender, instance, **kwargs):

    if instance.user:
        instance.user.delete()


#  create a signal for sending out emails when a new user signs up