from django.shortcuts import render

def business(request):
    return render(request,"index.html")
def login(request):
    return render(request,"login.html")
def signup(request):
    return render(request,"signup.html")
def asset(request):
    return render(request,"asset.html")
def business_management(request):
    return render(request,"business_management.html")
