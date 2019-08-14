from django.contrib import admin
from django.urls import path,re_path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
	re_path('login/',login_views,name='login'),
	re_path('register/',register_views,name='register'),
	re_path('index/',index_views),
]