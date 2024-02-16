from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Reg

# Create your views here.
class Home(View):
    def get(self,request):
        return render(request, template_name='home.html')

class RegInput(View):
    def get(self,request):
        return render(request, template_name='reginput.html')

class LoginInput(View):
    def get(self,request):
        return render(request, template_name='logininput.html')

class Register(View):
    def post(self,request):
        fn = request.POST["t1"]
        ln = request.POST["t2"]
        un = request.POST["t3"]
        pwd = request.POST["t4"]
        cpwd = request.POST["t5"]
        mobno = int(request.POST["t6"])
        email = request.POST["t7"]
        r1 = Reg(FirstName=fn,LastName=ln,UserName=un,password=pwd,cpassword=cpwd,MobileNumber=mobno,Emailid=email)
        r1.save()
        return HttpResponse("registration success")


class Login(View):
    def post(self,request):
        uname1 = request.POST["un"]
        password1 = request.POST["pwd"]
        res = Reg.objects.filter(UserName=uname1,password=password1)
        if res:
            return HttpResponse("Login success")
        else:
            return HttpResponse("Login failed")

