# urls.py
from django.urls import path
from .views import asset_management
from .views import add_asset

urlpatterns = [
    path('asset_management/', asset_management, name='asset_management'),
    path('add_asset/',add_asset, name='add_asset'),
]
