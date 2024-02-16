from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,template_name='input.html')

def add(request):
    x = int(request.POST["t1"])
    y = int(request.POST["t2"])
    z = x+y
    con_dict = {"res": z}
    return render(request, template_name='result.html',context=con_dict)