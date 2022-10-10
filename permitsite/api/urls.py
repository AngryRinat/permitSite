from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.UserAPIList.as_view()),
    path('users/<int:pk>/', views.UserAPIList.as_view()),
    path('usersdetail/<int:pk>', views.UserAPIDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
