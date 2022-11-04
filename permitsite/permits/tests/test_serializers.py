from django.test import TestCase
from permits.models import Permit
from api.serializers import PermitSerializer
from django.contrib.auth.models import User



class PermitSerializerTestCase(TestCase):
    def test_ok(self):
        user_1 = User.objects.create(username='dalek')
        permit_1 = Permit.objects.create(car_number='O999SF888', customer=User.objects.get(id=user_1.id))
        permit_2 = Permit.objects.create(car_number='O756SF888', customer=User.objects.get(id=user_1.id))
        data = PermitSerializer([permit_1, permit_2], many=True).data
        print(data)
        expected_data = [
            {"car_number":"O999SF888","is_active":"true"},
            {"car_number":"O756SF888","is_active":"true"},
        ]
        print(expected_data)
        self.assertEqual(data, expected_data)