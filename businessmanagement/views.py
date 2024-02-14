from django.shortcuts import render

def business(request):
    return render(request,"index.html")
def login(request):
    return render(request,"login.html")
def signup(request):
    return render(request,"signup.html")
def business_management(request):
    return render(request,"business_management.html")
def add_company(request):
    return render(request,"scrap_supply_management.html" )
def asset_management(request):
    return render(request,"asset_management.html")
def scrap_supply_management(request):
    return render(request,"scrap_supply_management.html")
