from django.shortcuts import render

# Create your views here.
from app.forms import *

def registation(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}
    return render(request,'registation.html',d)