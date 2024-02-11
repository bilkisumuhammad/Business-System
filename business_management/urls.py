from django.urls import path
from .views import business_management
from .views import create_business

urlpatterns = [
    path('business-management/', business_management, name='business_management'),
    path('create_business/', create_business, name='create_business'),
]