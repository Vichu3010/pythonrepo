from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'home.html',{'links':'http://127.0.0.1:8000/'})


def products(request):
    return render(request, 'index.html',
                  {'products': products})


def customers(request):
    return render(request, 'customers.html',
                  {'customers': customers})