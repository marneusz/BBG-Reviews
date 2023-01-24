from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.core.mail import EmailMultiAlternatives, send_mail
from django.shortcuts import redirect, render
from django.template import Context
from django.template.loader import get_template

from .forms import UserRegisterForm

# Create your views here.

# Index
def index(request):
    return render(request, "user/index.html", context={"title": "index"})


# Register
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")

            # Email Message
            html_template = get_template("user/email.html")
            d = {"username": username}
            subject, from_email, to_whom = "Welcome", "bbg.reviews.app@gmail.com", email
            html_content = html_template.render(d)
            message = EmailMultiAlternatives(
                subject, html_content, from_email, [to_whom]
            )
            message.attach_alternative(html_content, "text/html")
            message.send()

            messages.success(
                request,
                f"Your account has been successfully created! You are now able to log in.",
            )

            return redirect("login")

    else:
        form = UserRegisterForm()

    return render(
        request, "user/register.html", context={"form": form, "title": "Register here"},
    )


def login_(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {username}!")
            return redirect("index")
        else:
            UserModel = get_user_model()
            try:
                UserModel.objects.get(username=username)
                messages.error(request, f"Incorrect password.")
            except UserModel.DoesNotExist:
                messages.error(request, f"Account with this username does not exist.")
            form = AuthenticationForm()
    else:
        form = AuthenticationForm()
    return render(request, "user/login.html", context={"form": form, "title": "Log in"})


class PasswordResetView(PasswordResetView):
    template_name = "user/password_reset.html"
    form_class = PasswordResetForm

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        print("")
        self.extra_context.update({"email": email})
        return super().form_valid(form)
