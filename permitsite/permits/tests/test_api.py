from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from permits.models import Permit
from api.serializers import PermitSerializer


class PermitApiTestCase(APITestCase):
    def test_get(self):
        user_1 = User.objects.create(username='dalek')
        permit_1 = Permit.objects.create(car_number='O999SF888', customer=User.objects.get(id=user_1.id))
        permit_2 = Permit.objects.create(car_number='O756SF888', customer=User.objects.get(id=user_1.id))
        url = reverse('permit-list')
        response = self.client.get(url)
        serializer_data=PermitSerializer([permit_1, permit_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)