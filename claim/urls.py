from claim import views
from django.urls import path 

urlpatterns = [
    path('', views.claim, name = 'claim'),
    path('view_claims.html', views.view_claims, name = 'view_claims')
]