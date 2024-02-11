from django.shortcuts import render, redirect
from.forms import CompanyForm, MaterialDeliveryForm

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
