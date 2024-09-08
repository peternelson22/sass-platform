from django.contrib import admin
from .models import Subscription, UserSubscription, SubscriptionPrice

class SubscriptionPrice(admin.StackedInline):
    model = SubscriptionPrice
    readonly_fields = ['stripe_id']
    can_delete = False
    extra = 0
class SubscriptionAdmin(admin.ModelAdmin):
    inlines = [SubscriptionPrice]
    readonly_fields = ['stripe_id']
    list_display = ['name', 'active']
    
    
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(UserSubscription)

# Register your models here.
