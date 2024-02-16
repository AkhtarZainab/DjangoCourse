from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, template_name='input.html')

def calculate(request):
    x = int(request.GET["t1"])
    y = int(request.GET["t2"])
    operation = request.GET["op"]
    res = None
    if operation == 'add':
        res = "Sum: "+str(x+y)
    elif operation == 'sub':
        res = "Sub: "+str(x-y)
    elif operation == 'mul':
        res = "mul: "+str(x*y)
    else:
        res = "div: "+str(x/y)
    con_dict = {"result": res}
    return render(request,template_name='result.html',context=con_dict)