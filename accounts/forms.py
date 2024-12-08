from django import forms
from .models import Profile


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'email']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # getting user instance
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        profile = super().save(commit=False)  # get profile instance but no save yet

        if commit:
            profile.save()

        return profile