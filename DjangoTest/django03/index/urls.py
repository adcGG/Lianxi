from django.contrib import admin
from django.urls import path,re_path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
	re_path(r'01-parent',parent_views),
	re_path(r'02-child',child_views),
]