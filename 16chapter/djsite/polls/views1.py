from django.shortcuts import render
from django.http import HttpResponse        # 为访问的URL用户返回指定内容，在浏览器中显示
def index(request):
	return HttpResponse("Hello,world!You're at the polls index")

# Create your views here.
