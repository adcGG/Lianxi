from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.
def test_views(request):
	return HttpResponse("测试首页视图")

def temp_views(request):
	# 通过loader加载模板
	t = loader.get_template('01temp.html')
	# 将模板渲染成字符串
	html = t.render()
	# 再通过HttpResponse将字符串响应给浏览器
	return HttpResponse(html)

def temp02_views(request):
	str = "模板中的变量，字符串"
	num = 3306
	tup = ("谢逊","韦一笑","殷素素","金花婆婆")
	list_name = ["AA","BB","CC","DD","EE"]
	dic = {
		"BJ":"BJ",
		"AA":"AA",
		"CC":"CC",
	}
	say = sayHi()
	dog = Dog()
	return render(request,'01temp.html',locals())

def sayHi():
	return "Hello,this is a view"

class Dog(object):
	name = "GG"
	def eat(self):
		return "吃狗粮"

def static_views(request):
	return render(request,'04_static.html')

def index_views(request):
	return render(request,'index.html')