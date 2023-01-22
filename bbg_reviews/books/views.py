from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Review, Book, Author
from .forms import ReviewForm, BookForm, AuthorForm
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.


def book_list(request):
    book_list = Book.objects.order_by("-title")
    context = {"book_list": book_list}
    return render(request, "books/book_list.html", context)


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    form = ReviewForm()
    return render(request, "books/book_detail.html", {"book": book, "form": form})


def review_list(request):
    latest_review_list = Review.objects.order_by("-pub_date")[:9]
    context = {"latest_review_list": latest_review_list}
    return render(request, "books/review_list.html", context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, "books/review_detail.html", {"review": review})


@login_required
def add_review(request):
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.user = request.user
        review.book = Book.objects.get(pk=request.POST["book_id"])
        review.pub_date = datetime.datetime.now()
        review.save()
        return HttpResponseRedirect(reverse("review_detail", args=(review.id,)))
    return render(request, "books/book_detail.html", {"form": form})


@login_required
def add_book(request):
    if request.method == "POST":
        # handle form submission
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("book_list"))
    else:
        form = BookForm()

    return render(request, "books/add_book.html", {"form": form})


@login_required
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("book_list"))

    else:
        form = AuthorForm()
    return render(request, "books/add_author.html", {"form": form})

