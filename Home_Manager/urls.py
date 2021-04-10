"""Home_Manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com /en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from Home_Manager import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'home'),
    path('about_us/', include('about_us.urls')),
    path('complaint/', include('complaint.urls')),
    path('claim/', include('claim.urls')),
    path('rewards/', include('rewards.urls')),
    path('account/', include('account.urls')),
    path('user/', include('user_app.urls'))
] 

# static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
