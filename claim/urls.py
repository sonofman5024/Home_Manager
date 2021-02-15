from claim import views
from django.urls import path 

urlpatterns = [
    path('', views.claim, name = 'claim'),
]