from django.shortcuts import render
from django.http import HttpResponse
# request handler
# Create your views here.
# request --> response

def say_hello (request):
    #Pull data
    return render(request,'hello.html')