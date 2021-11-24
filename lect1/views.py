from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Django. Lecture 1 </h1>')


def hello(request):
    return render(request, "lect1/index.html")

def hello_name(request, name):
    return render(request, "lect1/greet.html", {
        "name": name.capitalize()
    })


