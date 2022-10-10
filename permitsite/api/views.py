from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api.serializers import UserSerializer

from users.models import User


class UserAPIList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserAPIDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


