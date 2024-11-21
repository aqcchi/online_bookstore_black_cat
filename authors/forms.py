from django import forms
from authors.models import Author


class AuthorAddForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorEditForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
