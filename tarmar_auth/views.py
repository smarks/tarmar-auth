from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import RegisterForm


class RegisterView(CreateView):
    """Create an account and sign the new user straight in."""

    form_class = RegisterForm
    template_name = "tarmar_auth/register.html"
    success_url = reverse_lazy("tarmar_auth:profile")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class ProfileView(LoginRequiredMixin, TemplateView):
    """The signed-in user's own profile."""

    template_name = "tarmar_auth/profile.html"
