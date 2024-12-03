from django import forms
from authors.models import Author


class AuthorAddForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

    picture = forms.URLField(
        widget=forms.TextInput(attrs={'placeholder': "Enter URL with the author's image"}),
        required=False,
    )


class AuthorEditForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

    picture = forms.URLField(
        widget=forms.TextInput(attrs={'placeholder': "Enter URL with the author's image"}),
        required=False,
    )