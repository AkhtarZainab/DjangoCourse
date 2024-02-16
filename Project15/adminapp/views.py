from django.shortcuts import render
from django.views import View
from .models import Product
# Create your views here.

class DisplayView(View):
    def get(self,request):
        qs = Product.objects.all()
        con_dict = {'records':qs}
        return render(request, template_name='display.html', context=con_dict)
