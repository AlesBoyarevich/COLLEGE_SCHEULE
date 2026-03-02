"""
URL configuration for COLLEGE_SCHEDULE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from teachers.urls import urlpatterns as teacher_urls
from core.urls import urlpatterns as core_urls
from schedule.urls import urlpatterns as schedule_urls
from groups.urls import urlpatterns as groups_urls
from subjects.urls import urlpatterns as subjects_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core_urls)),
    path('schedule/', include(schedule_urls)),
    path('teachers/', include(teacher_urls)),
    path('groups/', include(groups_urls)),
    path('subjects/', include(subjects_urls)),
]
