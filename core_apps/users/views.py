from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer


class CustomUserDetailsView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = IsAuthenticated

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        return get_user_model().objects.none()


# kkk@mail.com
# kkklll
