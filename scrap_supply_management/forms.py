from django import forms
from .models import Company, MaterialDelivery

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name']

class MaterialDeliveryForm(forms.ModelForm):
    class Meta:
        model = MaterialDelivery
        fields = ['company','truck', 'weight_kg', 'cost_per_kg', 'payment_recieved']
