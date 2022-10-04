from rest_framework.serializers import ModelSerializer

from permits.models import Permit


class PermitSerializer(ModelSerializer):
    class Meta:
        model = Permit
        fields = '__all__'