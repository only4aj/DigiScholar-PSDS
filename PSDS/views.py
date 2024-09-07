from django.shortcuts import render
from dotenv import load_dotenv
import os
# Create your views here.


def home(request):
    # Password Load from .env file
    # load_dotenv()
    return render(request , "home.html" )#,{"key":os.environ.get("PASSWORD")})
    # pass


def login(request):
    return render(request , "login.html")

def scholarship(request):
    return render(request , "scholarship.html")

def sag_bureau(request):
    pass

def finance_bureau(request):
    pass