from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('hello/', views.hello, name='hello page'),
    path('hello/<str:name>', views.hello_name, name='name'),
]