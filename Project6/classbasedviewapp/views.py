from django.shortcuts import render
from django.views import View

# Create your views here.
class GetInput(View):
    def get(self,request):
        return render(request,template_name='getinput.html')

class PostInput(View):
    def get(self,request):
        return render(request,template_name='postinput.html')

class Add(View):
    res = None
    def get(self,request):
        x = int(request.GET["t1"])
        y = int(request.GET["t2"])
        res = "Sum: "+str(x+y)
        con_dict = {"result":res}
        return render(request,template_name='result.html',context=con_dict)

