from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import SignUpView, SignInView, MeView

urlpatterns = [
    path("auth/sign-up/", SignUpView.as_view()),
    path("auth/sign-in/", SignInView.as_view()),
    path("auth/refresh/", TokenRefreshView.as_view()),
    path("auth/me/", MeView.as_view(), name="me"),
]