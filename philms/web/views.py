from django.http import HttpResponse
from django import forms

def index(request):
    
    reponse = HttpResponse("Welcome to philms.")
    
