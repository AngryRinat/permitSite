from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from rest_framework.viewsets import ModelViewSet

from permits.forms import PermitCreateForm
from permits.models import Permit
from permits.serializers import PermitSerializer



class PermitViewSet(ModelViewSet):
    queryset = Permit.objects.all()
    serializer_class = PermitSerializer

class PermitCreateView(CreateView):
    form_class = PermitCreateForm
    template_name = 'permits/permits_create.html'
    success_url = reverse_lazy('permits:index')

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)




def permits_user_list(request):
    permitlist = Permit.objects.filter(customer = request.user, is_active = True)
    context = {
        'permitlist': permitlist,
        'title': 'Пропуска'
    }
    return render(request, 'permits/permits_list_view.html', context)

class PermitsArchiveList(ListView):
    model = Permit
    template_name = 'permits/permits_list_view.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permitlist'] = Permit.objects.filter(customer = self.request.user, is_active = False)
        context['title'] = 'Пропуска в архиве'
        return context


def permits_main_page(request):
    title = 'PermitSite'
    context = {
        'title': title
    }
    return render(request, 'permits/permits_main_page.html', context)

class PermitControlView(ListView):
    model = Permit
    template_name = 'permits/permits_list_control.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        search_by = self.request.GET.get('search_by')
        query = self.request.GET.get('query')
        search_message = 'All phones'
        if search_by in ['phone', 'name'] and search_by:
            if search_by == 'name':
               permitlist = Permit.objects.filter(customer__username=query)
               search_message = f'Searching for "name" by "{query}"'
            else:
               permitlist = Permit.objects.filter(car_number=query)
               search_message = f'Searching for "phones" by "{query}"'
        else:
             permitlist = Permit.objects.all()
        context["permitlist"] = permitlist
        context["search_message"] = search_message
        return context


def permit_deactivate(request, id):
    permit = Permit.objects.get(id=id)
    permit.is_active = False
    permit.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])



