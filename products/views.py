from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello Mooki')


def new(request):
    return HttpResponse('New line')
