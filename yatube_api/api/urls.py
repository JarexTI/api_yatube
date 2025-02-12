from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import (CommentViewSet, GroupViewSet, PostViewSet,
                    UserRegistrationView, UserViewSet)

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('register/', UserRegistrationView.as_view()),
]
