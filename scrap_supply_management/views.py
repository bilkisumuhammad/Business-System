from django.shortcuts import render, redirect
from.forms import CompanyForm,MaterialDeliveryForm
from .forms import CompanyForm
from .models import Company

def scrap_supply(request):
    form = CompanyForm()
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('scrap_supply')
        else:
            form = CompanyForm()

    companies = Company.objects.all()  # Fetch all companies
    context = {'form': form, 'companies': companies}
    return render(request, 'scrap_supply_management.html', context)

    

def add_material_details(request):
    form = MaterialDeliveryForm()
    if request.method =='POST':
    
        form = MaterialDeliveryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('scrap_supply')
        #Redirect to a company list page
        else:
            form = MaterialDeliveryForm()

    context = {'form':form}
    return render(request, 'add_material_details.html',context)


def display_total_cost(request, company_id):
    company = Company.objects.get(pk=company_id)
    total_cost = company.calculate_total_cost()

    context = {
        'company': company,
        'total_cost': total_cost,
    }

    return render(request, 'display_total_cost.html', context)

