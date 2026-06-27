from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """A minimal, project-agnostic user for shared login.

    Consuming projects set ``AUTH_USER_MODEL = "tarmar_auth.User"``. It is a
    plain :class:`~django.contrib.auth.models.AbstractUser` so the shared login
    flow stays generic; keep project-specific data in your own models.
    """
