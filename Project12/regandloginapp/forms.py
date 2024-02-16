from django import forms
from .models import Reg

class RegForm(forms.ModelForm):
    class Meta:
        model = Reg
        fields = ['FirstName','LastName','UserName','password','cpassword','MobileNumber','Emailid']
        widgets = {'password':forms.PasswordInput(),'cpassword':forms.PasswordInput()}

class LoginForm(forms.Form):
    UserName = forms.CharField(max_length=10)
    Password = forms.CharField(max_length=10, widget=forms.PasswordInput())
