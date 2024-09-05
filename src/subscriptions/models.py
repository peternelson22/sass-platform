from django.db import models

class Subscription(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        permissions = [
            ('basic', 'Basic Plan'),
            ('advanced', 'Advanced Plan'),
            ('pro', 'Pro Plan'),
        ]
        