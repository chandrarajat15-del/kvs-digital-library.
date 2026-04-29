from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'), # Added name='search' here
    path('upload/', views.teacher_upload, name='teacher_upload'),
]

