from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests

def welcome(request):
    template_name = "frontend/homepage.html"
    
    return render(request, template_name)
