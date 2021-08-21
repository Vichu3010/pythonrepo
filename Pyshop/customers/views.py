from django.shortcuts import render
from django.http import HttpResponse
from .models import Customers


def customers(request):
    customer = Customers.objects.all()
    return render(request, 'customers.html',
                  {'customers': customer})


def new(request):
    return HttpResponse('New project')






