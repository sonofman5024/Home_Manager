from account import views
from django.urls import path 

urlpatterns = [
    path('', views.account, name = 'account'),
    path('account_info/', views.account_info, name = 'account_info'),
]