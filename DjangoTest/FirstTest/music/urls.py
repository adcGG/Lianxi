from django.contrib import admin
from django.urls import path,re_path
from .views import *
urlpatterns = [
    # path('admin/', admin.site.urls),
	# 当访问路劲是index的时候交给index_views处理
	re_path(r'^index/',index_views)
]