from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if (not self.request.user.is_authenticated):
            return redirect_to_login(self.request.get_full_path())
        if not self.has_permission():
            return redirect('/permits')
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    adress = models.CharField(max_length=200, blank=True, null=True)
    contacts = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.user)
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwagrs):
    if created:
        Profile.objects.create(user=instance)
        print('Profile created!')

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):

    if created == False:
        instance.profile.save()
        print('Profile updated!')