from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
  # return HttpResponse("Hello world I'm Home")
  return render(request, 'home.html')

def aboutpage(request):
  # return HttpResponse("Hello about page, I am in about")
  return render(request, 'about.html')