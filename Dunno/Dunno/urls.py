from django.urls import path, include
from rest_framework import routers
from posts.api.views.post_views import ListPosts
from posts.api.views.comment_views import (
    CommentListCreateAPIView,
    CommentDetailsAPIView,
)

from posts.views import upvote_a_post, redirect_post_link


router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("/comments/", CommentListCreateAPIView),
    path(
        "api-auth/", include("rest_framework.urls", namespace="rest_framework")
    ),
    path("posts/", ListPosts.as_view()),
    path(
        "comments/",
        CommentListCreateAPIView.as_view(),
        name="api-comment-list",
    ),
    path("posts/id_<str:pk>", ListPosts.as_view()),
    path("comments/id_<str:pk>", CommentDetailsAPIView.as_view()),
    path("posts/upvote_<str:identificator>/", upvote_a_post),
    path("posts/link_<str:identificator>/", redirect_post_link),
]
