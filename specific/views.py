from django.shortcuts import render

# Create your views here.

def spec1(request):
    return render(request,'spec1.html')

def spec2(request):
    return render(request,'spec2.html')