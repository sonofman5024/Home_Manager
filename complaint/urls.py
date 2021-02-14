from complaint import views
from django.urls import path 

urlpatterns = [
    path('', views.complaint, name = 'complaint'),
]