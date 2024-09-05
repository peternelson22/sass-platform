from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def profile_view(request, username=None, *args, **kwargs):
    user = request.user
    
    user_profile = get_object_or_404(User, username=username)
    is_me = user_profile == user

    return HttpResponse(f"Hello profile {is_me}")

def profile_detail_view(request, *args, **kwargs):
    user = request.user
    # user_groups = user.groups.all()
    print(user.has_perm('subscriptions.basic'), 
          user.has_perm('subscriptions.pro'), 
          user.has_perm('subscriptions.advanced'))
    # if user_groups.filter(name__icontains='basic').exists():
    #     return HttpResponse('Basic Plan')
    return HttpResponse(f"Hello profile")