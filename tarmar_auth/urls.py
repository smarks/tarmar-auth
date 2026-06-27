from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import ProfileView, RegisterView

app_name = "tarmar_auth"

urlpatterns = [
    path("login/", LoginView.as_view(template_name="tarmar_auth/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
