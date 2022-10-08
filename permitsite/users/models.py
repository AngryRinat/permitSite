from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def safe_delete(self):
        self.is_active = False
        self.save()