from django.urls import path
from .views import list, list_companies

urlpatterns = [
   path('list/<str:list_name>/', list, name='list'),
   path('list_companies/', list_companies, name='list_companies'),
]
