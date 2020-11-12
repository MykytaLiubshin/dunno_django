from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from posts.api.views.post_views import PostListCreateAPIView, PostDetailsAPIView

from posts.views import upvote_a_post

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path(r"/posts/", PostListCreateAPIView),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('posts/', PostListCreateAPIView.as_view(), name='api-post-list'),
    path('posts/upvote_<str:identificator>/', upvote_a_post),
]
