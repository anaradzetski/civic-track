from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter


from .views import ReportViewSet, SignUpView, SignInView, MeView

router = DefaultRouter()
router.register(r"reports", ReportViewSet, basename='router')

urlpatterns = [
    path("auth/sign-up/", SignUpView.as_view()),
    path("auth/sign-in/", SignInView.as_view()),
    path("auth/refresh/", TokenRefreshView.as_view()),
    path("auth/me/", MeView.as_view(), name="me"),
    path("", include(router.urls))
]