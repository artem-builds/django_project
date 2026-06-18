from django.shortcuts import render
from django.http import HttpResponse

def about_me(request):
    return HttpResponse("This is about page")