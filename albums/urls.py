from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('demo1', views.demo1, name='demo1'),
]