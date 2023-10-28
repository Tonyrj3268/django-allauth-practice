from django.shortcuts import render

# Create your views here.

from allauth.account.views import LoginView


class CustomLoginView(LoginView):
    template_name = "custom_login.html"  # your custom template


def home(request):
    return render(request, "base.html")
