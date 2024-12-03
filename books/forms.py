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

    price = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter the book price in USD',
            'min': '0.01',
        }),
    )

    image_url = forms.URLField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter URL with the cover image'}),
        required=False,
    )


class BookEditForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.SelectMultiple,
    )


