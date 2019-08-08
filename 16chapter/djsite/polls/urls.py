from django.urls import path
from . import views1
urlpatterns = [
	path("",views1.index,name = 'index'),
]

