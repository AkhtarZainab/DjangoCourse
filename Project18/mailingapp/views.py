from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
# import random
# Create your views here.

def email_send(request):
    subject='lokesh it'
    email_message=str('Hello..how you doing..?')
    From_mail=settings.EMAIL_HOST_USER
    to_list=['zainabakhtar27@gmail.com','seemaakh321@gmail.com']
    send_mail(subject,email_message,From_mail,to_list,fail_silently=False)
    return HttpResponse("email sent successfully")