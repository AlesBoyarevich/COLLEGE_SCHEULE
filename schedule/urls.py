from django.urls import path
from . import views


urlpatterns = [
    path('teachers/', views.Teachers.as_view(), name='teachers'),
    path('subjects/', views.Subjects.as_view(), name='subjects'),
    path('groups/', views.Groups.as_view(), name='groups'),
    path('schedule/', views.Schedule.as_view(), name='schedule'),
]
