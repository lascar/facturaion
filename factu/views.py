from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from companies.models import Company
from staff_members.models import StaffMember

def list_companies(request):
    companies = Company.objects.all()
    template = loader.get_template('companies.html')
    context = {
        'companies': companies,
    }
    return HttpResponse(template.render(context, request))

def list(request, list_name: str):
    breakpoint()
    return render(
        request,
        "home.html",
        {"new_item_text": request.POST["item_text"]},
    )
