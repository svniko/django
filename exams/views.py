from django.shortcuts import render
from django.http import HttpResponse
import datetime;
# from django.conf import settings as django_settings
# import os


import matplotlib.pyplot as plt
import io
import urllib, base64


def index(request):
    now = datetime.datetime.now()
    date = datetime.datetime.now().date
    is_exam = now.month == 1 and now.day >= 10 and now.day <= 31
    return render(request, "exams/index.html", {
        "exams": is_exam,
        "date": date,
    })

    
def matplot(request):
    x= range(10)
    y = range(10)
    # plt.plot(range(10))
    plt.plot(x,y)
    # fig = plt.gcf()
    #convert graph into dtring buffer and then we convert 64 bit code into image
    buf = io.BytesIO()
    plt.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri =  urllib.parse.quote(string)
    return render(request,'exams/index.html',{'data':uri})

def matplot_save(request):
    x= range(5)
    y = range(5)
    plt.plot(x,y)
    
   
    plt.savefig('exams/static/exams/image.png',dpi = 300)
    # os.path.join(SITE_ROOT, 'templates/')
    # plt.savefig(os.path.join(django_settings.STATIC_ROOT, '/exams/image.png'), dpi=300) 

    return render(request,'exams/index.html')