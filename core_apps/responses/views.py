from django.shortcuts import render
from rest_framework import generics
from .models import Article, Responses
from .serializers import ResponseSerializer
from rest_framework.exceptions import PermissionDenied
from rest_framework import permissions
from django.shortcuts import get_object_or_404


class ResponseListCreateView(generics.ListCreateAPIView):
    queryset = Responses.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ResponseSerializer

    def get_queryset(self):
        article_id = self.kwargs.get('article_id')
        return Responses.objects.filter(article__id=article_id, parent_response=None)

    def perform_create(self, serializer):
        user = self.request.user
        article_id = self.kwargs.get('article_id')
        article = get_object_or_404(Article, id=article_id)
        serializer.save(user=user, article=article)


class ResponseUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Responses.objects.all()
    serializer_class = ResponseSerializer
    lookup_field = "id"

    def perform_update(self, serializer):
        user = self.request.user
        response = self.get_object()
        if user != response.user:
            raise PermissionDenied("You don't have permission to edit this response")
        serializer.save()


    def perform_destroy(self, instance):
        user = self.request.user
        response = self.get_object()
        if user != response.user:
            raise PermissionDenied("You don't have permission to delete this response")
        instance.delete()
