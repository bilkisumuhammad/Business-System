from django.urls import path
from .views import business_management

urlpatterns = [
    path('business-management/', business_management, name='business_management'),
]