# views.py
from django.shortcuts import render

def asset_management(request):
    # Logic for handling asset management
    return render(request, 'asset_management.html')
def add_asset(request):
    return render(request,'asset_management.html')
def add_additional_cost(request):
    return render(request, 'add_cost_additional_cost.html')
