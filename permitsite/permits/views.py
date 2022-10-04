from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, TemplateView
from rest_framework.viewsets import ModelViewSet

from permits.models import Permit
from permits.serializers import PermitSerializer


class PermitViewSet(ModelViewSet):
    queryset = Permit.objects.all()
    serializer_class = PermitSerializer

class PermitCreateView(CreateView):
    model = Permit
    fields = '__all__'
    template_name = 'permits/permits_create.html'
    success_url = reverse_lazy('permits:index')


class PermitListView(ListView):
    model = Permit
    template_name = 'permits/permits_list_view.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permitlist'] = Permit.objects.get(all)
        context['title'] = 'Главная страница'
        return context


def permits_main_page(request):
    title = 'PermitSite'
    context = {
        'title': title
    }
    return render(request, 'permits/permits_main_page.html', context)
