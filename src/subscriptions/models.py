from django.db import models
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_save
from django.conf import settings


User = settings.AUTH_USER_MODEL

ALLOW_CUSTOM_GROUPS = True
SUBSCRIPTION_PERMISSIONS = [
    ('basic', 'Basic Plan'),
    ('advanced', 'Advanced Plan'),
    ('pro', 'Pro Plan'),
]
class Subscription(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    groups = models.ManyToManyField(Group)
    permissions =  models.ManyToManyField(Permission, limit_choices_to={
        "content_type__app_label": "subscriptions", "codename__in": [x[0] for x in SUBSCRIPTION_PERMISSIONS]
        }
    )
    
    def __str__(self) -> str:
         return self.name
    class Meta:
        permissions = [
            ('basic', 'Basic Plan'),
            ('advanced', 'Advanced Plan'),
            ('pro', 'Pro Plan'),
        ]
    
class UserSubscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True, blank=True)
    active = models.BooleanField(default=True)  
    

def user_sub_post_save(sender, instance, *args, **kwargs):
    user_sub_instance = instance
    user = user_sub_instance.user
    subscription_obj = user_sub_instance.subscription
    groups_ids = []
    if subscription_obj is not None:
        groups = subscription_obj.groups.all()
        groups_ids = groups.values_list('id', flat=True)
    if not ALLOW_CUSTOM_GROUPS:
        user.groups.set(groups_ids)
    else:
        subscription_qs = Subscription.objects.filter(active=True)
        if subscription_obj is not None:
            subscription_qs = subscription_qs.exclude(id=subscription_obj.id)
        subscription_groups = subscription_qs.values_list('groups__id', flat=True)
        subscription_groups_set = set(subscription_groups)
        # groups_ids = groups.values_list('id', flat=True)
        current_groups = user.groups.all().values_list('id', flat=True)
        groups_ids_set = set(groups_ids)
        current_groups_set = set(current_groups) - subscription_groups_set
        final_group_ids = list(groups_ids_set | current_groups_set)
        user.groups.set(final_group_ids)
    
post_save.connect(user_sub_post_save, sender=UserSubscription)
    