from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('signin/', views.Signin.as_view(), name='signin'),
    path('logout/', views.Logout.as_view(), name='logout'),
]