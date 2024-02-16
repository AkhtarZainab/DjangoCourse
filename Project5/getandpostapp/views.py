from django.shortcuts import render

# Create your views here.
def getinput(request):
    return render(request,template_name='getinput.html')

def postinput(request):
    return render(request,template_name='postinput.html')

def add(request):
    res = None
    if request.method == "GET":
        x = int(request.GET["t1"])
        y = int(request.GET["t2"])
        res = "Sum: "+str(x+y)
    else:
        x = int(request.POST["t1"])
        y = int(request.POST["t2"])
        res = "Sum: " + str(x + y)
    con_dict = {"result":res}
    return render(request,template_name='result.html',context=con_dict)

