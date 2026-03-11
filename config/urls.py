from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.tasks.views import TaskViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from apps.core.views import RegisterView
from apps.core.views import RegisterView, MeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("apps.tasks.urls")),
    path("api/auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/auth/register/", RegisterView.as_view(), name="register"),
    path("api/auth/me/", MeView.as_view(), name="me"),
]