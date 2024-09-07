from django.urls import path
from PSDS import views

urlpatterns = [
    path('' , views.home , name = 'home'),
    path('scholarship/' , views.scholarship , name = 'scholarship'),
    path('applypmsss/' , views.scholarship_form , name = 'scholarship_form'),
    path('docsupload/' , views.docs_upload , name = 'docs_upload'),
    path('login/' , views.login , name = 'login')
]
