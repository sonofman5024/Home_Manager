from user_app import views
from django.urls import path 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/parent/', views.register, name = 'register'),
    path('signup/preregister/', views.pre_register, name = 'pre_register'),
    path('signup/kid/', views.register_kid, name = 'register_kid'),
    path('signup/kid/parent_conf/', views.parent_conf, name = 'parent_conf'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name = 'login'),
    path('kids_login/', auth_views.LoginView.as_view(template_name='login_kid.html'), name = 'login_kid'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name = 'logout'),
    path('signup/', views.fork, name = 'fork'),
    path('thank_you.html', views.thank_you, name = 'thank_you'),
]