"""effusion_a_cappella URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
import events.views
import members.views
import videos.views
import emailsender.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', events.views.home, name='home'),
    path('events', events.views.events, name='events'),
    path('members', members.views.members, name='members'),
    path('videos', videos.views.videos, name='videos'),
    path('contact', emailsender.views.sendemail, name='emailsender')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
