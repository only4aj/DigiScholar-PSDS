from django.urls import path
from PSDS import views

urlpatterns = [
    path('' , views.home , name = 'home'),
    path('scholarship/' , views.scholarship , name = 'scholarship'),
    path('login/' , views.login , name = 'login')
]
