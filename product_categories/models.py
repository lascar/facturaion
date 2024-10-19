from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from facturaion.models import TimeStampedModel
from companies.models import Company
import pdb

''' :model:categories.Category '''
class ProductCategory(TimeStampedModel):

    name = models.CharField(max_length=100)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.name
