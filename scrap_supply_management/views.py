from django.shortcuts import render, redirect
from.forms import CompanyForm, MaterialDeliveryForm


def scrap_supply_management(request):
    return render(request, 'scrap_supply_management.html')
def add_company(request):
    return render(request, 'scrap_supply_management')


def add_company(request):
    if request.method =='POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_list')
        #Redirect to a company list page
        else:
            form = CompanyForm()
            return render(request,'add_company.html',{'form':form})


# Create your views here.
