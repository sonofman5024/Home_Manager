from account import views
from django.urls import path 

urlpatterns = [
    path('', views.account, name = 'account'),
    path('account_info/', views.account_info, name = 'account_info'),
    path('account_info/<kid_id>', views.kid_claim, name = 'kid_claim'),
    path('account_info/accept/<claim_id>', views.accept, name = 'accept'),
    path('account_info/decline/<claim_id>', views.decline, name = 'decline'),
]