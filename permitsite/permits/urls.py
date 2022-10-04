from django.urls import path

from permits.views import PermitCreateView, permits_main_page, PermitListView

app_name = 'permits'

urlpatterns = [
    path('create', PermitCreateView.as_view(), name='create'),
    path('', permits_main_page, name='index'),
    path('archive', PermitListView.as_view(), name='archive')
]
