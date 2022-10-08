from django.urls import path

from permits.views import PermitCreateView, permits_main_page, permits_user_list, PermitsArchiveList, PermitControlView, permit_deactivate

app_name = 'permits'

urlpatterns = [
    path('create', PermitCreateView.as_view(), name='create'),
    path('', permits_main_page, name='index'),
    path('list', permits_user_list, name='list'),
    path('archive', PermitsArchiveList.as_view(), name='archive'),
    path('control', PermitControlView.as_view(), name='control'),
    path('permit-remove/<int:id>/', permit_deactivate, name='permit_deactivate')
]
