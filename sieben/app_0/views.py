from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def simp_resp(request):
    return HttpResponse("Simplest http")