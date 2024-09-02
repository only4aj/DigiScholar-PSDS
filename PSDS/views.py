from django.shortcuts import render
from dotenv import load_dotenv
import os
# Create your views here.


def index(request):
    # Password Load from .env file
    load_dotenv()
    return render(request , "index.html",{"key":os.environ.get("PASSWORD")})
    # pass


def login(request):
    pass

def sag_bureau(request):
    pass

def finance_bureau(request):
    pass