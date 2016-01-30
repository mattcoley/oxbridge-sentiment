from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return render(request, 'sentiment/index.html', {})

def data(request):
    return render(request, 'sentiment/data.html', {})
