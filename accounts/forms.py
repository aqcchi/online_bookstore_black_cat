from django import forms
from .models import Profile


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the user instance
        super().__init__(*args, **kwargs)
        if user:
            self.fields['email'].initial = user.email  # Pre-fill email field with the user's current email

    def save(self, commit=True):
        profile = super().save(commit=False)  # Get the profile instance but don't save yet
        profile.user.email = self.cleaned_data['email']  # Update the associated user's email field

        if commit:
            profile.user.save()  # Save the updated User instance with the new email
            profile.save()  # Save the Profile instance

        return profile  # Return the updated Profile instance
