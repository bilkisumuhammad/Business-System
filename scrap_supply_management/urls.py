from django.urls import path
from .views import scrap_supply_management
from .views import add_company

urlpatterns = [
path('scrap_supply_management/', scrap_supply_management, name='scrap_supply_management'),
path('add_company/', add_company, name='add_company'),
]