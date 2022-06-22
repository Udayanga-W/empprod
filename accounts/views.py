import imp
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse()

def about(request):
    return render(request,'accounts/about.html')


def leaves(request):
    return render(request,'accounts/leaves.html')

def users(request):
    return render(request,'accounts/userunderme.html')

