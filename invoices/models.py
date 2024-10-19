from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.utils.translation import gettext as _
from facturaion.models import TimeStampedModel
from companies.models import Company
from staff_members.models import StaffMember
from customers.models import Customer
import pdb

'''  :model:`invoices.Invoice`, has a :model:`customers.Customer` and can have :model:`staff.StaffMember` and :model:`invoices.InvoiceLine` '''
class Invoice(TimeStampedModel):
    STATUS = (
        ('draft', _(u'Draft')),
        ('sent', _(u'Sent')),
        ('paid', _(u'Paid')),
        ('canceled', _(u'Canceled')),
    )
    PAYMENT_STATUS = (
        ('wholly_paid', _(u'Wholly paid')),
        ('party_paid', _(u'Partially paid')),
        ('not_paid', _(u'Not paid')),
        ('on_due_date', _(u'On due date')),
    )
    invoice_number = models.CharField(max_length=100, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    staff_member = models.ForeignKey(StaffMember, on_delete=models.PROTECT, blank=True, null=True)
    amount_before_vat = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid_before_vat = models.DecimalField(max_digits=10, decimal_places=2)
    amount_after_vat = models.DecimalField(max_digits=10, decimal_places=2)
    amount_after_after_vat = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    wholly_paid = models.BooleanField(default=False)
    wholly_paid_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, editable=False,
                               choices=STATUS,
                               default='draft')
    payment_status = models.CharField(max_length=20, editable=False,
                                      choices=PAYMENT_STATUS,
                                      default='due_on_date')
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=False)


    def __str__(self):
        return self.invoice_number

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
