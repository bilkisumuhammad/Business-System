# views.py
from django.shortcuts import render, redirect
from .models import Asset
from .form import AssetForm

def asset_management(request):
    # Logic for handling asset management
    return render(request, 'asset_management.html')

def asset_list(request):
    assets = Asset.objects.all()
    return render(request,'asset_list.html',{'assets':assets})
def add_asset(request):
    if request.method =='POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset_list')
        else:
            form = AssetForm()
            return render(request,'add_asset.html',{'form': form})
            

