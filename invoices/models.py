from django.db import models

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20)
    date = models.DateField()
    customer_name = models.CharField(max_length=100)

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, related_name="details", on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def line_total(self):
        return self.quantity * self.price
