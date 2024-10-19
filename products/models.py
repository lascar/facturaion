from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.utils.translation import gettext as _
from facturaion.models import TimeStampedModel
from companies.models import Company
from product_categories.models import ProductCategory
import pdb

''' :model:products.Product, can have a category of :model:`product_categories.ProductCategory` '''
class Product(TimeStampedModel):

    TYPE = (
        ('product', _(u'Product')),
        ('service', _(u'Service')),
    )
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, null=True, blank=True)
    description = models.TextField()
    type = models.CharField(max_length=20, editable=False,
                            choices=TYPE,
                            default='product')
    unit_price_before_vat = models.DecimalField(max_digits=10, decimal_places=2)
    vat_rate = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return f'{self.name} - {self.type}{self.category.name if self.category else""}'

    def is_due(self):
        return self.due_date < timezone.now()

    def is_paid(self):
        return self.wholly_paid

    def mark_as_paid(self):
        self.wholly_paid = True
        self.wholly_paid_date = timezone.now()
        self.status = 'paid'
        self.payment_status = 'wholly_paid'
        self.save()

    def is_paid_late(self):
        return self.wholly_paid_date > self.due_date

    def is_paid_on_time(self):
        return self.wholly_paid_date <= self.due_date

    def is_paid_within_30_days(self):
        return self.paid_date <= self.due_date + timedelta(days=30)
