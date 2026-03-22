from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  # return HttpResponse("Hello, world, You are at rohit home")
  return render(request,'website/index.html')

def about(request):
  # return HttpResponse("for about")
  return render(request,"website/about.html")

def contact(request):
  # return HttpResponse("for contact")
  return render(request,"website/contact.html")