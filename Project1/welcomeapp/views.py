from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    res = HttpResponse('''<html><body bgcolor=cyan><h1><center>Welcome to LokeshIT</center></h1></body></html>''')
    return res