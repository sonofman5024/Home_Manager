from claim import views
from django.urls import path 

urlpatterns = [
    path('', views.claim, name = 'claim'),
    path('file_claim.html', views.file_claim, name = 'file_claim'),
    path('thank_you.html', views.thank_you, name = 'thank_you'),
    path('claim_history.html', views.claim_history, name = 'claim_history'),
    path('delete/<claim_id>', views.delete, name = 'delete'),
    path('edit/<claim_id>', views.edit, name = 'edit'),
]