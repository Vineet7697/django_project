"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'),
    path('redirect1/',views.redirect1,name='redirect1'),
    path('redirect3/',views.redirect3,name='redirect3'),
    path('redirect4/',views.redirect4),
    path('redirect5/',views.redirect5,name='redirect5'),
    path('redirect6/<str:name>/',views.redirect6,name='redirect6'),
    path('redirect7_permanently/',views.redirect7_permanently,name='redirect7_permanently'),
]
