from account import views
from django.urls import path 

urlpatterns = [
    path('', views.account, name = 'account'),
]