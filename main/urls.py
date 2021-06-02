from django.urls import path, include
from .views import trending

urlpatterns = [
    path('trending-repos/', trending),
]
