from django.urls import path
from .views import add_material_details, scrap_supply, display_total_cost

urlpatterns = [
    path('', scrap_supply, name='scrap_supply'),
    path('add_material/', add_material_details, name='add_material'),
    path('display_total_cost/<int:company_id>/', display_total_cost, name='display_total_cost'),
]
