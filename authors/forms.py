from django import forms
from authors.models import Author


class BaseAuthorForm(forms.ModelForm):
    picture = forms.URLField(
        widget=forms.TextInput(attrs={'placeholder': "Enter URL with the author's image"}),
        required=False,
    )

    class Meta:
        model = Author
        fields = '__all__'


class AuthorAddForm(BaseAuthorForm):
    pass


class AuthorEditForm(BaseAuthorForm):
    pass
