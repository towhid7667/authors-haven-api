from django.urls import path

from .views import BookmarkCreateView, BookMarkDestroytView

urlpatterns = [
    path(
        "bookmark_article/<uuid:article_id>/",
        BookmarkCreateView.as_view(),
        name="bookmark_article",
    ),
    path(
        "remove_bookmark/<uuid:article_id>/",
        BookMarkDestroytView.as_view(),
        name="remove_bookmark",
    ),
]
