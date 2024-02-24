from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def calculate_total_cost(self):
        material_deliveries = MaterialDelivery.objects.filter(company=self)
        total_cost = sum(delivery.total_cost for delivery in material_deliveries)
        return total_cost

class MaterialDelivery(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    truck = models.CharField(max_length=50)
    weight_kg = models.DecimalField(max_digits=10, decimal_places=2)
    cost_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    payment_received = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.company} - {self.delivery_date}"
        
