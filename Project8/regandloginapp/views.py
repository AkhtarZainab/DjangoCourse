from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,template_name='home.html')

class RegInput(View):
    def get(self,request):
        return render(request,template_name='reginput.html')

class LoginInput(View):
    def get(self,request):
        return render(request,template_name='logininput.html')

class Register(View):
    def post(self,request):
        return HttpResponse("registration success")

class Login(View):
    def post(self,request):
        return HttpResponse("Login success")

