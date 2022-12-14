"""permitsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter


from permits.views import PermitViewSet

router = SimpleRouter()

router.register(r'permit', PermitViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('permits/', include('permits.urls', namespace='permits')),
    path('users/', include('users.urls', namespace='users')),
    path('api/v1/', include('api.urls')),
]


urlpatterns += router.urls