from django.urls import path, include
from main import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('rsop2018', views.index, name='rsop'),
    path('rsop2018/projects', views.index, name='rsop-projects'),
]
