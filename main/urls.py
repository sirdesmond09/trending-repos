from django.urls import path, include
from .views import trending_repos

urlpatterns = [
    path('trending-repos/', trending_repos),
]
