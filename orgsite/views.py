from django.shortcuts import render, get_object_or_404
from .models import Organization

def home(request):
    orgs = Organization.objects.all().order_by('Org_Name')
    context = {
        'orgs': orgs
    }
    return render(request, 'home.html', context=context) 