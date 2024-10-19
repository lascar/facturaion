from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from facturaion.models import TimeStampedModel
from companies.models import Company
import pdb

'''  :model:`contacts.Contact`, stores contact information for customers, staff_members and companies '''
class Contact (TimeStampedModel):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=False)
