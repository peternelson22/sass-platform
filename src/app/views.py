from django.shortcuts import render, redirect
from visits.models import PageVisit
from django.contrib.auth.decorators import login_required

VALID_CODE = '123'

@login_required
def home(request):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    
    PageVisit.objects.create(path=request.path)
    context = {'page_visit_count': qs.count(), 'total_visit_count': page_qs.count()}
    return render(request, 'home.html', context)

def protected_view(request, *args, **kwargs):
    is_allowed = request.session.get('protected_page_allowed') or 0
    
    if request.method == 'POST':
        user_pw_sent = request.POST.get('code') or None
        if user_pw_sent == VALID_CODE:
            is_allowed = 1
            request.session['protected_page_allowed'] = is_allowed
    if is_allowed:
        return render(request, 'protected/view.html')
    return render(request, 'protected/entry.html')