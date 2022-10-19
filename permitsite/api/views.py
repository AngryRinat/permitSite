from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api.serializers import PermitSerializer
from permits.models import Permit
from rest_framework.permissions import IsAuthenticated


class PermitAPIList(ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = PermitSerializer

    def get_queryset(self):
        return Permit.objects.filter(customer=self.request.user, is_active=True)

    def perform_create(self, serializer):
        serializer.save(customer_id=self.request.user.id)


class UserAPIDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Permit.objects.all()

    serializer_class = PermitSerializer


class PermitUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Permit.objects.all()
    serializer_class = PermitSerializer
