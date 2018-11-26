from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_courses, name='list_courses'),
    path('student/add/', views.add_student, name='add_student')
]
