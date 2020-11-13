from django.urls import path
from posts.api.views.comment_views import ListComments


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", ListComments.as_view()),
    path("id_<str:pk>", ListComments.as_view()),
    path("post_<str:post>", ListComments.as_view()),
]
