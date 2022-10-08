from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegistrationForm, UserLoginForm


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('permits:index'))


class UserCreate(CreateView):
    form_class = UserRegistrationForm
    template_name = 'users/user_registration.html'
    success_url = reverse_lazy('permits:index')
    title = 'Регистрация'

    # def form_valid(self, form):
    #     user = form.save()


class UserLogin(LoginView):
    template_name = 'users/user_registration.html'
    form_class = UserLoginForm


    def get_success_url(self):
        return reverse_lazy('permits:index')