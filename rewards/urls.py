from rewards import views
from django.urls import path 

urlpatterns = [
    path('', views.rewards, name = 'rewards'),
]