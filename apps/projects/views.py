from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    return HttpResponse("There are projects")
