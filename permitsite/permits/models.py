from django.contrib.auth.models import User
from django.db import models

class Permit(models.Model):
    car_number = models.CharField(max_length=15)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
