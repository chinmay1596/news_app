# news/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('results/<int:search_id>/', views.results, name='results'),
    path('refresh_results/<int:search_id>/', views.refresh_results, name='refresh_results'),
    path('search_list/', views.search_list, name='search_list'),
]