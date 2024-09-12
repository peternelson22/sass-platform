import helpers.numbers
from django.shortcuts import render
from visits.models import PageVisit

from dashboard.views import dashboard_view

def landing_page_view(request):
    if request.user.is_authenticated:
        return dashboard_view(request)
    qs = PageVisit.objects.all()
    page_views_formatted = helpers.numbers.shorten_number(qs.count() * 100_000)
    social_page_views_formatted = helpers.numbers.shorten_number(qs.count() * 40_000)
    organization_views_formatted = helpers.numbers.shorten_number(qs.count() * 500)
    PageVisit.objects.create(path=request.path)
    context = {'page_views_count': page_views_formatted, 
               'social_views_count': social_page_views_formatted,
               'organization_views_count': organization_views_formatted
               }
    return render(request, 'landing/main.html', context)