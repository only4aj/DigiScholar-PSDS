from django.urls import path
from PSDS import views

urlpatterns = [
    path('' , views.index , name = 'index')
]
