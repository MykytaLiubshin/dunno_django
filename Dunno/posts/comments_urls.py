from django.urls import path
from posts.api.views.comment_views import ListComments


urlpatterns = [
    path("", ListComments.as_view()),
    path("id_<str:pk>", ListComments.as_view()),
    path("post_<str:post>", ListComments.as_view()),
]
