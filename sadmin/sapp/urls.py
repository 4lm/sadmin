from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course/add/', views.course_details, name='add_course'),
    path('course/edit/<int:pk>/', views.course_details, name='edit_course'),
    path('student/add/', views.student_details, name='add_student'),
    path('student/edit/<int:pk>/', views.student_details, name='edit_student')
]
