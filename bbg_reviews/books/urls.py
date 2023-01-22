from django.urls import path

from . import views

urlpatterns = [
    path("book_list/", views.book_list, name="book_list"),
    path("add_book/", views.add_book, name="add_book"),
    path("add_author/", views.add_author, name="add_author"),
    path("book_list/<int:book_id>/", views.book_detail, name="book_detail"),
    path("reviews/", views.review_list, name="review_list"),
    path("reviews/<int:review_id>/", views.review_detail, name="review_detail"),
    path("reviews/add/", views.add_review, name="add_review"),
]
