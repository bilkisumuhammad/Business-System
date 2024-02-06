from django import forms
from.models import BusinessCategory,CostInvested,Business

class BusinessCategoryForm(forms.ModelForm):
    class Meta:
        model = BusinessCategory
        fields = ['name','description']

class CostInvestedForm(forms.ModelForm):
    class Meta:
        model = CostInvested
        fields = ['amount']


class BusinessForm(forms.ModelForm):
    class Mete:
        model = Business
        fields = ['name','category','location','cost_invested']

        def __init__(self, *args,**Kwargs):
                    super().__init__(*args,**Kwargs)
                    self.fields['category'].queryset = BusinessCategory.objects.all()                
                              