# urls.py
from django.urls import path
from .views import asset_management
from .views import asset_list,add_asset


urlpatterns = [
    path('asset_management/', asset_management, name='asset_management'),
    path('assets/', asset_list, name='asset_list'),
    path('add_asset/', add_asset, name='add_asset'),
]
