from django.http import HttpResponse


def show_views(request):
	return HttpResponse("我的第一个Django程序")

def show1_views(request,num1): # 表示show/后面的第一个参数,传进来的都是字符串
	return HttpResponse("参数为"+num1+"的两位数啊")

def sh(request):
	return HttpResponse("正则表达式")

def show_bir_day(request,year,month,day):
	return HttpResponse("生日为：%s年%s月%s日"%(year,month,day))

def show3(request,name,age):
	return HttpResponse("名字：%s，年龄：%s"%(name,age))