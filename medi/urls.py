from django.urls import path
from . import views



urlpatterns = [
    path('get-medi/',views.get_medi)
]