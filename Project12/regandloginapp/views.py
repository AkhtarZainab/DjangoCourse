from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Reg
from .forms import RegForm,LoginForm

# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,template_name='home.html')

class RegInput(View):
    def get(self,request):
        con_dict = {"regform":RegForm()}
        return render(request,template_name='reginput.html',context=con_dict)


class LoginInput(View):
    def get(self,request):
        con_dict = {"loginform":LoginForm()}
        return render(request,template_name='logininput.html',context=con_dict)


class Register(View):
    def post(self,request):
        rf = RegForm(request.POST)
        if rf.is_valid():
            rf.save()
            return HttpResponse("registration success")


class Login(View):
    def post(self, request):
        lf = LoginForm(request.POST)
        if lf.is_valid():
            uname1 = lf.cleaned_data["UserName"]
            password1 = lf.cleaned_data["Password"]
            res = Reg.objects.filter(UserName=uname1,password=password1)
            if res:
                return HttpResponse("login success")
            else:
                return HttpResponse("login failed")

