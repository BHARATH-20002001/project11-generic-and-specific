from django.shortcuts import render

# Create your views here.

def gen1(request):
    return render(request,'gen1.html')

def gen2(request):
    return render(request,'gen2.html')