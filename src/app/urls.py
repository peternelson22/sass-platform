
from django.contrib import admin
from django.urls import path, include
from .views import home, protected_view
from auth.views import login_view, register_view
from subscriptions.views import subscription_price_view, user_subscription_view
from checkouts.views import checkout_finalize_view, product_price_redirect_view, checkout_redirect_view

urlpatterns = [
    path('', home, name='home'),
    # path('login/', login_view, name='login'),
    # path('register/', register_view, name='register'),
    path("checkout/sub-price/<int:price_id>/", product_price_redirect_view, name='sub-price-checkout'),
    path("checkout/start/", checkout_redirect_view, name='stripe-checkout-start'),
    path("checkout/success/", checkout_finalize_view, name='stripe-checkout-end'),
    path('protected/', protected_view, name='protected'),
    path('accounts/', include('allauth.urls')),
    
    path('accounts/billing/', user_subscription_view, name='user_subscription'),
    path('pricing/', subscription_price_view, name='pricing'),
    path('pricing/<str:interval>/', subscription_price_view, name='pricing_interval'),
    path('profile/', include('profiles.urls')),
    path('admin/', admin.site.urls),

]
