from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import (
    PostViewSet,
    UserViewSet,
    UserRegistrationView,
    GroupViewSet,
    CommentViewSet,
)

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts\/\d+\/comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('register/', UserRegistrationView.as_view()),
]
