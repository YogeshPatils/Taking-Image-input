from django.shortcuts import render
from django.http import HttpResponse
from .models import BikeModel
from .forms import BikeForm
# Create your views here.

def addBikeView(request):
    fm=BikeForm()
    if request.method=='POST' and request.FILES:
        fm=BikeForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            return HttpResponse('Bike Succesufully added....')
    return render(request,'index.html',{'form':fm})

def ShowBike(request):
    qs=BikeModel.objects.all()
    return render(request,'bike.html',{'bikes':qs})
