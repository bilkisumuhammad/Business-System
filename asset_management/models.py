from django.db import models

class Asset(models.Model):
    name = models.CharField(max_length=255)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    additional_costs = models.DecimalField(max_digits=10, decimal_places=2, default=10)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    purchase_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Calculate total amount when saving
        self.total_amount = self.purchase_price + self.additional_costs
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
