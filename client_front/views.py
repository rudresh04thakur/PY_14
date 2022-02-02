from re import template
from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('client_front/index.html')
    context = { 'name':'Mahesh'}
    return HttpResponse(template.render(context,request))
def register(request):
    template = loader.get_template('client_front/register.html')
    context = {}
    return HttpResponse(template.render(context,request))