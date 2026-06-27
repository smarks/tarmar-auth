from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    """Username + optional email registration, against the active user model."""

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email")
