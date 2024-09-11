import helpers.billing

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from subscriptions.models import SubscriptionPrice, UserSubscription
from subscriptions import utils as subs_utils 

@login_required
def user_subscription_view(request,):
    user_sub_obj, created = UserSubscription.objects.get_or_create(user=request.user)
    if request.method == "POST":
        print("refresh sub")
        finished = subs_utils.refresh_active_users_subscriptions(user_ids=[request.user.id], active_only=False)
        if finished:
            messages.success(request, "Your plan details have been refreshed.")
        else:
            messages.error(request, "Your plan details have not been refreshed, please try again.")
        return redirect(user_sub_obj.get_absolute_url())
    return render(request, 'subscriptions/user_detail_view.html', {"subscription": user_sub_obj})

@login_required
def user_subscription_cancel_view(request, *args, **kwargs):
    user_sub_obj, created = UserSubscription.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        if user_sub_obj.stripe_id and user_sub_obj.is_active_status:
            sub_data = helpers.billing.cancel_subscription(user_sub_obj.stripe_id, reason='User wanted to end', 
                                                           feedback='other', cancel_at_period_end=True, raw=False)
            for k, v in sub_data.items():
                setattr(user_sub_obj, k, v)
            user_sub_obj.save()
            messages.success(request, 'Your plan has been cancelled')
        return redirect(user_sub_obj.get_absolute_url())
    
    return render(request, 'subscriptions/user_cancel_view.html', {'subscription': user_sub_obj})


def subscription_price_view(request, interval='month'):
    qs = SubscriptionPrice.objects.filter(featured=True)
    monthly = SubscriptionPrice.IntervalChoices.MONTHLY
    yearly = SubscriptionPrice.IntervalChoices.YEARLY
    object_list = qs.filter(interval=monthly)
    
    url_path_name = 'pricing_interval'
    monthly_url = reverse(url_path_name, kwargs={'interval': monthly})
    yearly_url = reverse(url_path_name, kwargs={'interval': yearly})
    active = monthly
    
    if interval == yearly:
        active = yearly
        object_list = qs.filter(interval=yearly)
    context = {'object_list': object_list, 'monthly_url': monthly_url, 'yearly_url': yearly_url, 'active': active}
    return render(request, 'subscriptions/pricing.html', context)