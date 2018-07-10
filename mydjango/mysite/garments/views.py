from django.shortcuts import render
from garments.models import FormalShirt 
from garments.models import CausualShirt
from garments.models import TShirt
from garments.models import Trouser
from garments.models import Jean
from garments.models import TrackPant
# Create your views here.
def index(request):
    return render(request,'index.html') #takes max of 3 parameters synatx(request(url),template,dictonary(to pass values to template)) ,all templates are html files,render means execute
    

def aboutus(request):
    return render(request,'aboutus.html')

def formal_shirts(request):
    lst=FormalShirt.objects.all()
    return render(request,'formal_shirts.html',{'lst':lst})

def causual_shirts(request):
    lst=CausualShirt.objects.all()
    return render(request,'causual_shirts.html',{'lst':lst})

def t_shirts(request):
    lst=TShirt.objects.all()
    return render(request,'t_shirts.html',{'lst':lst})

def trouser(request):
    lst=Trouser.objects.all()
    return render(request,'trouser.html',{'lst':lst})

def jean(request):
    lst=Jean.objects.all()
    return render(request,'jean.html',{'lst':lst})
def track_pant(request):
    lst=TrackPant.objects.all()
    return render(request,'track_pant.html',{'lst':lst})


    

