from django.urls import path
from . import views

app_name = "exams"

urlpatterns = [
    path("", views.index, name="index"),
    path("matplot/", views.matplot, name='matpolt'),
    path("matplot_save/", views.matplot_save, name='matpolt_save')
]