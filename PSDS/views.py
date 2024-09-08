from django.shortcuts import render
from dotenv import load_dotenv
from django.conf import settings
import os
import rsa
# Create your views here.

def home(request):
    load_dotenv()
    PKey = getattr(settings,"PUBLICKEY")
    data = rsa.encryptionData(PKey,os.environ.get("PKEY"),"This is Home Directory")
    
    return render(request , "home.html" )#,{"key":os.environ.get("PASSWORD")})
    # pass


def login(request):
    return render(request , "login.html")

def scholarship(request):
    return render(request , "scholarship.html")

def scholarship_form(request):
    return render(request , "scholarship_form.html")

def docs_upload(request):
    return render(request , "docsupload.html")

def sag_bureau(request):
    pass

def finance_bureau(request):
    pass