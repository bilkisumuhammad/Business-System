from django.contrib import admin
from .models import BusinessCategory,CostInvested,Business

# Register your models here.
admin.site.register(BusinessCategory)
admin.site.register(CostInvested)
admin.site.register(Business)

