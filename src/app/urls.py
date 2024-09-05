
from django.contrib import admin
from django.urls import path, include
from .views import home, protected_view
from auth.views import login_view, register_view

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('protected/', protected_view, name='protected'),
    path('accounts/', include('allauth.urls')),
    path('profile/', include('profiles.urls')),
    path('admin/', admin.site.urls),

]
