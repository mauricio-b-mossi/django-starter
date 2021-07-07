"""django_course_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django_course_site.settings import MEDIA_ROOT, MEDIA_URL
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # create user through terminal
    # python manage.py createsuperuser in this app my username is mauri and password is mauri
    path('admin/', admin.site.urls),
    # path('*', include('devfolder.urls'))
    path('', include('meetups.urls'))
    # To serve static files add a + and concat their address to the list
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
