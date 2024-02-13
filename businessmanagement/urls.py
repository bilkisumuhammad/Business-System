"""
URL configuration for businessmanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from businessmanagement.views import business, business_management, asset_management
from login.views import signup, user_login




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',business, name='business'), # Name added for the business view
    path('account/', include('login.urls')), 
    path('business_management/', include('business_management.urls')), 
    path('asset_management/', include('asset_management.urls')),
    
      
    
]

