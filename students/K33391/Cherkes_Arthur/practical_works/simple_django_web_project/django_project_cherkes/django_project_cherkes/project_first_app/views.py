from django.shortcuts import render, redirect

# Create your views here.
from django.http import Http404
from django.shortcuts import render
from project_first_app.models import Owner
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django import forms

from .forms import OwnerForm
from .models import Car


def get_all_owners_info(request):
    context = {'owners': Owner.objects.all()}
    return render(request, 'owners.html', context)


def get_owner_info(request, owner_id):
    try:
        context = {'owner': Owner.objects.get(owner_id=owner_id)}
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', context)


def create_owner(request):
    context = {}

    if request.method == "POST":
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("owners")
    else:
        form = OwnerForm()
        context['form'] = form
        return render(request, "create_update_view.html", context)


class CarView(DetailView):
    model = Car
    template_name = 'car.html'


class CarListView(ListView):
    model = Car
    queryset = model.objects.all()
    template_name = 'cars.html'


class CarUpdateView(UpdateView):
    model = Car
    fields = ['color']
    success_url = '/cars/'
    template_name = 'create_update_view.html'


class CarCreateView(CreateView):
    model = Car
    fields = ['car_id', 'brand', 'model', 'color']
    success_url = '/cars/'
    template_name = 'create_update_view.html'


class CarDeleteView(DeleteView):
    model = Car
    success_url = '/cars/'
    template_name = 'delete_view.html'