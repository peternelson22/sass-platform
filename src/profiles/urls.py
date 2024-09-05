
from django.urls import path
from .views import profile_view, profile_detail_view

urlpatterns = [
    path('<str:username>/', profile_view, name='profile'),
    path('', profile_detail_view, name='profile_detail'),
]
