from django.shortcuts import render
from dotenv import load_dotenv
from django.conf import settings
import os
import rsa

# Create your views here.


def home(request):
    return render(request, "home.html")  # ,{"key":os.environ.get("PASSWORD")})


def login(request):
    return render(request, "login.html")


def scholarship(request):
    return render(request, "scholarship.html")


def scholarship_form(request):
    return render(request, "scholarship_form.html")


# Encryption Function
def encryptionData(data):
    load_dotenv()
    PKey = getattr(settings, "PUBLICKEY")
    return rsa.encryptionData(PKey, os.environ.get("PKEY"), data)


def docs_upload(request):
    studentName = request.POST.get("name", "")
    fatherName = request.POST.get("father_name", "")
    motherName = request.POST.get("mother_name", "")
    gender = request.POST.get("gender", "")
    email = request.POST.get("email", "")
    phone = request.POST.get("phone", "")
    dob = request.POST.get("dob", "")
    nationality = request.POST.get("nationality", "")
    permanent_address = request.POST.get("permanent_address", "")
    institution = request.POST.get("institution", "")
    course = request.POST.get("course", "")
    current_year = request.POST.get("current_year", "")
    course_type = request.POST.get("course_type", "")
    tenth_marks = request.POST.get("tenth_marks", "")
    tenth_percentage = request.POST.get("tenth_percentage", "")
    twelth_marks = request.POST.get("twelth_marks", "")
    twelth_percentage = request.POST.get("twelth_percentage", "")
    bank = request.POST.get("bank", "")
    account_number = request.POST.get("account_number", "")
    caccount_number = request.POST.get("caccount_number", "")
    ifsc = request.POST.get("ifsc", "")

    if not (
        studentName
        and fatherName
        and motherName
        and gender
        and email
        and phone
        and dob
        and nationality
        and permanent_address
        and institution
        and course
        and current_year
        and course_type
        and tenth_marks
        and tenth_percentage
        and twelth_marks
        and twelth_percentage
        and bank
        and account_number
        and caccount_number
        and ifsc
    ):
        return render(
            request, "scholarship_form.html", {"message": "Please fill all details!"}
        )

    try:
        ency_Name = encryptionData(studentName)
        ency_fatherName = encryptionData(fatherName)
        ency_motherName = encryptionData(motherName)
        ency_gender = encryptionData(gender)
        ency_email = encryptionData(email)
        ency_phone = encryptionData(phone)
        ency_dob = encryptionData(dob)
        ency_nationality = encryptionData(nationality)
        ency_address = encryptionData(permanent_address)
        ency_institution = encryptionData(institution)
        ency_course = encryptionData(course)
        ency_currentYear = encryptionData(current_year)
        ency_courseType = encryptionData(course_type)
        ency_tenthMarks = encryptionData(tenth_marks)
        ency_tenthPer = encryptionData(tenth_percentage)
        ency_twelthMarks = encryptionData(twelth_marks)
        ency_twelthPer = encryptionData(twelth_percentage)
        ency_bank = encryptionData(bank)
        ency_accNo = encryptionData(account_number)
        ency_caccNo = encryptionData(caccount_number)
        ency_ifsc = encryptionData(ifsc)

        print(ency_institution)
        print(ency_nationality)
        print(ency_Name)
        print(ency_fatherName)
        print(ency_motherName)
        print(ency_gender)
        print(ency_caccNo)
        print(ency_course)
        print(ency_tenthMarks)
        print(ency_email)
        print(ency_phone)
    except Exception:
        print("Some Error Occured!")
    return render(request, "docsupload.html")


def register(request):
    return render(request, "register.html")


def sag_bureau(request):
    pass


def finance_bureau(request):
    pass


def student_profile(request):
    return render(request , "userprofile.html")

def preview_page(request):
    return render(request , "preview.html")