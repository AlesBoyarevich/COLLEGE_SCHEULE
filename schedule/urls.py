from django.urls import path
from . import views


urlpatterns = [
    path('teachers/', views.Teachers.as_view(), name='teachers'),
    path('teachers/create/', views.TeachersCreate.as_view(), name='teachers create'),
    path('teachers/delete/<int:id>/', views.TeachersDelete.as_view(), name='teachers delete'),
    path('teachers/edit/<int:id>/', views.TeachersEdit.as_view(), name='teachers edit'),

    path('subjects/', views.Subjects.as_view(), name='subjects'),
    path('subjects/create/', views.SubjectsCreate.as_view(), name='subjects create'),
    path('subjects/delete/<int:id>/', views.SubjectsDelete.as_view(), name='subjects delete'),
    path('subjects/edit/<int:id>/', views.SubjectsEdit.as_view(), name='subjects edit'),

    path('groups/', views.Groups.as_view(), name='groups'),
    path('groups/create/', views.GroupsCreate.as_view(), name='groups create'),
    path('groups/edit/<str:group_name>/', views.GroupsEdit.as_view(), name='groups edit'),
    path('groups/delete/<str:group_name>/', views.GroupsDelete.as_view(), name='groups delete'),

    path('', views.Schedule.as_view(), name='schedule'),
]
