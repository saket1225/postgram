from django.shortcuts import render
from django.http import HttpResponse

def homePage(request):
    return render(request, "main/home.html/")
