# views.py
from django.shortcuts import render, redirect,get_object_or_404
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
            

def asset_overview(request):
    owned_assets = Asset.objects.all()
    return render(request, 'asset_overview.html', {'owned_assets': owned_assets})



# Add this new view
def asset_details(request, asset_id):
    asset = get_object_or_404(Asset, pk=asset_id)
    return render(request, 'asset_details.html', {'asset': asset})

#def remove_asset_view(request,asset_id):
   # asset = get_object_or_404(Asset,id=asset_id)
    #asset.delete()
    #return redirect('asset')

