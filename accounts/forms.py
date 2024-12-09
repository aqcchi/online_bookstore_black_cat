from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'email']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # getting user instance
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        profile = super().save(commit=False)  # getting profile instance but no save yet

        if commit:
            profile.save()

        return profile


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user