from django.urls import path

from . import views

app_name = 'shabbat'
urlpatterns = [
	path('english', views.index, name='index'),
	path('hebrew', views.index_hebrew, name='index_hebrew'),
	path('hello', views.hello, name='hello'),

]