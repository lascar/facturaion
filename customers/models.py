from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from facturaion.models import TimeStampedModel
from companies.models import Company
from contacts.models import Contact
import pdb

'''  :model:`customers.Customer`, can have a :model:`companies.Company` as from_company (where he works) and a list of :model:`contacts.Contact` for localisation '''
class Customer(TimeStampedModel):
    civility = models.CharField(max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contacts = models.ManyToManyField(Contact)
    from_company = models.ForeignKey('companies.Company', related_name='from_company', on_delete=models.PROTECT, null=True, blank=True)
    company = models.ForeignKey('companies.Company', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return f'{self.civility} {self.first_name} {self.last_name}{self.company.name if self.company else""}'
