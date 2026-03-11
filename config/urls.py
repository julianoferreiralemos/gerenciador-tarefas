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
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("apps.tasks.urls")),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/',SpectacularSwaggerView.as_view(url_name='schema'),name='swagger-ui'),
    path("api/auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/auth/register/", RegisterView.as_view(), name="register"),
    path("api/auth/me/", MeView.as_view(), name="me"),
    path("api/", include("apps.tasks.urls")),
    path("api/auth/", include("apps.accounts.urls")),
    path("api/tasks/", include("apps.tasks.urls")),
    path("api/auth/", include("apps.accounts.urls")),
]