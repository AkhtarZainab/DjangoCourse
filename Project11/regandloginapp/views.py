from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
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
        return render(request, template_name='logininput.html',context=con_dict)


class Register(View):
    def post(selfself,request):
        rf = RegForm(request.POST)
        if rf.is_valid():
            r1 = Reg(FirstName=rf.cleaned_data['FirstName'],
                     LastName=rf.cleaned_data['LastName'],
                     UserName=rf.cleaned_data['UserName'],
                     password=rf.cleaned_data['Password'],
                     cpassword=rf.cleaned_data['Cpassword'],
                     MobileNumber=rf.cleaned_data['MobileNumber'],
                     Emailid=rf.cleaned_data['EmailId'])
            r1.save()
            return HttpResponse("registration success")


class Login(View):
    def post(self,request):
        lf=LoginForm(request.POST)
        if lf.is_valid():
            uname1=lf.cleaned_data["UserName"]
            password1=lf.cleaned_data["Password"]
            res=Reg.objects.filter(UserName=uname1,password=password1)
            if res:
                return HttpResponse("Login success")
            else:
                return HttpResponse("Login failed")