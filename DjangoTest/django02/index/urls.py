from django.urls import re_path,path
from .views import *
urlpatterns = [
	re_path(r'^01-test',test_views),
	re_path(r'^01temp',temp_views),
	re_path(r'02temp',temp02_views),
	re_path(r'^04_static',static_views),
	re_path(r'^$',index_views),

]