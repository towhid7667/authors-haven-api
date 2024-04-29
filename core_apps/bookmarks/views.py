from rest_framework import generics, permissions
from .models import Bookmark
from .serializers import BookmarkSerializer
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError, NotFound
from core_apps.articles.models import Article

from uuid import UUID


class BookmarkCreateView(generics.CreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        article_id = self.kwargs.get('article_id')

        if article_id:
            try:
                article = Article.objects.get(id=article_id)
            except Article.DoesNotexist:
                raise ValidationError("article_id is not required")
        else:
            raise ValidationError("article_id is required")

        try:
            serializer.save(user=self.request.user, article=article)
        except IntegrityError:
            raise ValidationError("You have already bookmarked this article")

