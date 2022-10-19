from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('permits/', views.PermitAPIList.as_view()),
    path('drf-auth/', include('rest_framework.urls')),
    path('users/<int:pk>/', views.PermitAPIList.as_view()),
    path('permit-update/<int:pk>', views.PermitUpdateAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
