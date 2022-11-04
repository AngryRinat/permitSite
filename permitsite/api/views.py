from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from api.serializers import PermitSerializer
from permits.models import Permit
from rest_framework.permissions import IsAuthenticated


class PermitAPIList(ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = PermitSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['car_number']

    def get_queryset(self):
        return Permit.objects.filter(customer=self.request.user, is_active=True)

    def perform_create(self, serializer):
        serializer.save(customer_id=self.request.user.id)


class UserAPIDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Permit.objects.all()

    serializer_class = PermitSerializer


class PermitViewSet(ModelViewSet):
    queryset = Permit.objects.filter()
    serializer_class = PermitSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['car_number']
    search_fileds = ['car_number']
    ordering_fields =['car_number']
