
# urls.py
from django.urls import path
from .views import asset_overview, asset_management, asset_list, add_asset,asset_details

urlpatterns = [
    path('asset_overview/', asset_overview, name='asset_overview'),
    path('asset_management/', asset_management, name='asset_management'),
    path('assets/', asset_list, name='asset_list'),
    path('add_asset/', add_asset, name='add_asset'),
    path('assets/<int:asset_id>/', asset_details, name='asset_details'),
    #path('remove_asset/<int:asset_id>/',remove_asset_view,name='remove_asset'),
]
