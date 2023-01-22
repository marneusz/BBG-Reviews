from django.contrib import admin

# Register your models here.
from .models import Author, Book, Review

classes = [Author, Book, Review]

for model in classes:
    admin.site.register(model)
