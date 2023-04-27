from django.shortcuts import render
import datetime
# Create your views here.
def student(request):
    dt=datetime.datetime.now()
    d={'data':'hi hello hr u','dt':dt} 
   
    return render(request,'o.html',d)