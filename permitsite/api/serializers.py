from permits.models import Permit
from rest_framework import serializers



class PermitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permit
        fields = ['car_number', 'is_active']