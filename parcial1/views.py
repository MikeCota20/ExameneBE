from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

def home(request):
    return HttpResponse("Home")

def about(request):
    return HttpResponse("About")