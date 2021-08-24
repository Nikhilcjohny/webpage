# Create your views here
from django.shortcuts import render


def fun(request):
    return render(request,"index.html")