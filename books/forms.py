from django import forms
from authors.models import Author
from .models import Book


class BookAddForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    # for choosing more than one author at a time
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


class BookEditForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


