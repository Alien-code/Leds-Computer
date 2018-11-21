from django.db import models
from django.utils import timezone
from employee.models import Employee

# Model for entry customers order
class Order(models.Model):
    customer_name = models.CharField(max_length=60, default='Mr. ')
    contact = models.CharField(max_length=15, blank=True)
    item = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    qty = models.IntegerField()
    unit_price = models.IntegerField()
    # price_cal = unit_price * qty
    price = models.IntegerField()
    entry_time = models.DateTimeField(default=timezone.now())
    STATUS_CHOICE = (('Processing', 'Processing'),('Delivered', 'Delivered'))
    status = models.CharField(max_length=20, choices=STATUS_CHOICE)
    sale_by = models.OneToOneField(Employee, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.customer_name + "  - " + self.item + " - " + self.status
