from django.db import models
from django.conf import settings

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    summary = models.TextField(
        max_length=1000,
        help_text="Enter a brief description of the book",
    )

    # Model Meta is basically the inner class of your model class. Model Meta is basically used to change
    # the behavior of your model fields like changing order options,verbose_name, and a lot of other options.
    class Meta:
        ordering = ["-id"]

    def __str__(self) -> str:
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name}"


class Review(models.Model):
    RATING_CHOICES = (
        (i, str(i)) for i in range(10, 0, -1)
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Publication Date")
    comment = models.TextField(max_length=1024)
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)

    def __str__(self) -> str:
        return f"{self.book.title} - {self.user.username}, {self.rating}"

    class Meta:
        verbose_name = "Book Review"
        verbose_name_plural = "Book Reviews"
        ordering = ["-pub_date"]
        