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
    path('text_response1/',views.text_response1),
    path('html_response/',views.html_response),
    path('json_response',views.json_response),
    path('download_csv',views.download_csv),
    path('download_pdf',views.download_pdf),
    path('download_zip',views.download_zip),
    path('css_response',views.css_response),
    path('jpeg_image_response',views.jpeg_image_response),
    path('png_image_response',views.png_image_response),
    path('download_image',views.download_image),
    path('audio_response',views.audio_response),
    path('download_audio',views.download_audio),
    path('video_response',views.video_response),
    path('download_video',views.download_video),
]
