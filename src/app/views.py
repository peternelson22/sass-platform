from django.shortcuts import render, redirect
from visits.models import PageVisit

def home(request):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    
    PageVisit.objects.create(path=request.path)
    context = {'page_visit_count': qs.count(), 'total_visit_count': page_qs.count()}
    return render(request, 'home.html', context)