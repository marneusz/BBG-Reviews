"""bbg_reviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth
from django.urls import path, include
from user import views as user_view

from user.views import PasswordResetView

urlpatterns = [
    path("admin/", admin.site.urls),
    # user-related urls
    path("", include("user.urls")),
    path("login/", user_view.login_, name="login"),
    path(
        "logout/",
        auth.LogoutView.as_view(template_name="user/index.html"),
        name="logout",
    ),
    path("register/", user_view.register, name="register"),
    path("password_reset", PasswordResetView.as_view(), name="password_reset",),
    path(
        "password_reset/done",
        auth.PasswordResetDoneView.as_view(
            template_name="user/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>",
        auth.PasswordResetConfirmView.as_view(
            template_name="user/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done",
        auth.PasswordResetCompleteView.as_view(
            template_name="user/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    # app-related urls
    path("books/", include("books.urls"), name="books"),
]
