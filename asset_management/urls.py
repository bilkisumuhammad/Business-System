# urls.py
from django.urls import path
from .views import asset_management
from .views import add_asset
from .views import add_additional_cost

urlpatterns = [
    path('asset_management/', asset_management, name='asset_management'),
    path('add_asset/', add_asset, name='add_asset'),
    path('add_additional_cost/', add_additional_cost, name='add_additional_cost'),
]
