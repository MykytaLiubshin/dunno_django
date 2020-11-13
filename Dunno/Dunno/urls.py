from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path(
        "api-auth/",
        include("rest_framework.urls", namespace="rest_framework"),
    ),
    path("posts/", include("posts.posts_urls")),
    path("comments/", include("posts.comments_urls")),
]
