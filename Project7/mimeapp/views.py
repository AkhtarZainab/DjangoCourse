# from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
data = '''<table><tr><th>eid</th><th>ename</th><th>esal</th></tr>
<tr><td>1001</td><td>Scott</td><td>2000</td></tr>
<tr><td>1002</td><td>Blake</td><td>1500</td></tr>
<tr><td>1003</td><td>Miller</td><td>2500</td></tr>
</table>
'''

class htmlview(View):
    def get(self,request):
        return HttpResponse(data,content_type="text/html")

class excelview(View):
    def get(self,request):
        return HttpResponse(data,content_type="application/vnd.ms-excel")

class xmlview(View):
    def get(self,request):
        return HttpResponse(data,content_type="application/xml")