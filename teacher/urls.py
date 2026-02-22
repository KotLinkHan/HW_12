from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_page, name="teacher_page"),
    path('lessons', views.teacher_lessons, name="teacher_lessons"),
    path('lessons/<int:lesson_id>', views.specific_lesson, name="specific_lesson"),
    path('lessons/<int:lesson_id>/absence', views.absence, name="absence"),
    path('lessons/<int:lesson_id>/grade', views.grade, name="grade"),
    path('lessons/<int:lesson_id>/homework/<int:homework_id>', views.check_student_homework, name="check_student_homework"),
]
