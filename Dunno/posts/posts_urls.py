from django.urls import path
from posts.api.views.post_views import ListPosts
from posts.views import upvote_a_post, redirect_post_link


urlpatterns = [
    path("", ListPosts.as_view()),
    path("id_<str:identificator>", ListPosts.as_view()),
    path("upvote_<str:identificator>/", upvote_a_post),
    path("link_<str:identificator>/", redirect_post_link),
]
