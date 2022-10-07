from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']



class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('username', 'password')