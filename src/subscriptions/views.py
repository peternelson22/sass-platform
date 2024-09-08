from django.shortcuts import render
from django.urls import reverse
from subscriptions.models import SubscriptionPrice


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