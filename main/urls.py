from django.urls import path 
from .views import firstPage , clients , medicines , companies , bills , medical_bills
urlpatterns = [
    path('', firstPage , name= 'first_page'),
    path('clients/', clients , name= 'clients'),
    path('bills/', bills , name= 'bills'),
    path('companies/', companies , name= 'companies'),
    path('medicines/', medicines , name= 'medicines'),
    path('medical_bills/', medical_bills , name= 'medical_bills'),
]