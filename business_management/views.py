from django.shortcuts import render, redirect
from .forms import BusinessCategoryForm,CostInvestedForm,BusinessForm

def business_management(request):
    return render(request, 'business_management.html')


def create_business(request):

    business_form = BusinessForm()
    category_form = BusinessCategoryForm()
    cost_form = CostInvestedForm()

    if request.method == 'POST':
        business_form = BusinessForm(request.POST)
        category_form = BusinessCategoryForm(request.POST)
        cost_form = CostInvestedForm(request.POST)
        if business_form.is_valid():
            business_form.save()
            return redirect('create_business')

        elif cost_form.is_valid():
            cost_form.save()
            return redirect('create_business')

        elif category_form.is_valid():
             category_form.save()  
             return redirect('create_business')
        else:
            business_form = BusinessForm()
            category_form = BusinessCategoryForm()
            cost_form = CostInvestedForm()
    return render(request,'create_business.html',{'business_form':business_form, 'category_form':category_form, 'cost_form':cost_form})  
