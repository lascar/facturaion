from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.utils.translation import gettext as _
from facturaion.models import TimeStampedModel
from authentication.models import CustomUser
from companies.models import Company
from contacts.models import Contact
import pdb

'''  :model:`staff_members.StaffMember`, has a list of :model:`contacts.Contact` for localisation, can have a :model:`authentication.CustomUser` if he can login '''
class StaffMember(TimeStampedModel):

    ROLE = (
        ('manager', _(u'Manager')),
        ('accountant', _(u'Accountant')),
        ('staff', _(u'Staff')),
    )
    CIVILITY = (
        ('mr', _(u'Mr')),
        ('mrs', _(u'Mrs')),
        ('miss', _(u'Miss')),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    civility = models.CharField(max_length=20, editable=False,
                                choices=CIVILITY,
                                default='mr')
    contacts = models.ManyToManyField(Contact)
    role = models.CharField(max_length=20, editable=False,
                               choices=ROLE,
                               default='staff')
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.civility + ' ' + self.first_name + ' ' + self.last_name
