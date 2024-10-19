from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.utils.translation import gettext as _
from facturaion.models import TimeStampedModel
from products.models import Product
from companies.models import Company
from invoices.models import Invoice
import pdb

''' has a :model:`invoices.Invoice` and a :model:`products.Product` '''
class InvoiceLine(TimeStampedModel):

    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, blank=True, null=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount_before_vat = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.invoice.invoice_number + ' - ' + self.product.name
