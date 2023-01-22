from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from .models import Book, Review, Author


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("rating", "comment")


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("title", "author", "genre", "summary")


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ("first_name", "last_name")
