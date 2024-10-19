from django.db import models
from django.utils.translation import gettext as _
from facturaion.models import TimeStampedModel
import pdb

''' :model:companies.Company has a responsible_staff_member as responsible person '''
class Company(TimeStampedModel):

    company_registration_number = models.CharField(max_length=100, unique=True, primary_key = True)
    name = models.CharField(max_length=100)
    responsible_staff_member_id = models.IntegerField()

    def __str__(self):
        return self.name + ' - ' + self.company_registration_number
