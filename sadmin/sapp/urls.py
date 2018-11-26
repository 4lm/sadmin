from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_courses, name='list_courses'),
    path('student/add/', views.add_student, name='add_student'),
    path('course/add/', views.course_details, name='add_course'),
    path('course/edit/<int:pk>/', views.course_details, name='edit_course')
]
