from django.db import models

class BusinessCategory(models.Model):
    name = models.CharField(max_length=50,verbose_name='Category Name')
    description = models.TextField(blank=True,null=True, verbose_name='Category Description')

    def __str__(self):
        return self.name
    
class CostInvested(models.Model):
    amount =models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Amount')

    def __str__(self):
        return f"${self.amount}" 
    
class Business(models.Model):
    name = models.CharField(max_length=225,verbose_name='Business Name')
    category = models.ForeignKey(BusinessCategory,on_delete=models.CASCADE,verbose_name='Business Category') 
    location = models.CharField(max_length=225,verbose_name='Location')
    cost_invested= models.ForeignKey(CostInvested,on_delete=models.CASCADE,verbose_name='Cost Invested')

    def __str__(self):
        return self.name



