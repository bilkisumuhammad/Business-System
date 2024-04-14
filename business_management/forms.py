from django import forms
from .models import BusinessCategory,CostInvested,Business

class BusinessCategoryForm(forms.ModelForm):
    class Meta:
        model = BusinessCategory
        fields = '__all__' 

class CostInvestedForm(forms.ModelForm):
    class Meta:
        model = CostInvested
        fields = '__all__' 

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = '__all__' 

        def __init__(self, *args,**Kwargs):
            super().__init__(*args,**Kwargs)
            self.fields['category'].queryset = BusinessCategory.objects.all()                
     