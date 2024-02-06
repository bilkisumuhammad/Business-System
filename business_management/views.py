from django.shortcuts import render, redirect
from.forms import BusinessCategoryForm,CostInvestedForm,BusinessForm

def business_management(request):
    return render(request, 'business_management.html')


def create_business(request):
    if request.method == 'POST':
        business_form = BusinessForm(request.POST,prefix='business')
        category_form = BusinessCategoryForm(request.POST,prefix='category')
        cost_form = CostInvestedForm(request.POST,prefix='cost')

        if business_form.is_valid() and cost_form.is_valid():
                                                   # save the BusinessCategory instance 
            category_instance = category_form.save()
                                         # save the CostInvested instance
            cost_instance = cost_form.save()
                # save the Business instance with the related category and cost
            business_instance = business_form.save(commit=False)

            business_instance.category = category_instance

            business_instance.save ()
            return redirect('success_page')  # Redirect to a success page
        else:
            business_form = BusinessForm(prefix='business')
            category_form = BusinessCategoryForm(prefix='category')
            cost_form = CostInvestedForm(prefix='cost')

            return render(request,'business.html',{'business_form':business_form, 'category_form':category_form, 'cost_form':cost_form})   
