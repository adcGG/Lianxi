from django.shortcuts import render

# Create your views here.
def parent_views(request):
	list_head = ['首页','衣服','视频','婴儿']
	return render(request,'01-parent.html',locals())

def child_views(request):
	list_head = ['首页', '衣服', '视频', '婴儿']
	return render(request,'02-child.html',locals())
