from companies.models import Company
from staff_members.models import StaffMember
import pdb

class FactuCompanies:
    def __init__(self, companies):
      self.companies = companies

class FactuStaffMembers:
    def __init__(self, company_registration_number):
      self.staff_members = StaffMember.objects.filter(company__registration_number=company_registration_number)

    def get_staff_members(self):
      breakpoint()

