from django.urls import path

from users.views import user_logout, UserCreate, UserLogin

app_name = 'users'

urlpatterns = [
    path('logout', user_logout, name='logout'),
    path('register', UserCreate.as_view(), name='register'),
    path('login', UserLogin.as_view(), name='login')
]
