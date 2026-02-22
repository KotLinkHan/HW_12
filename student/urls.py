from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_page, name="student_page"),
    path("lessons", views.student_lesson, name="student_lesson"),
    path("lessons/<int:lesson_id>", views.student_specific_lesson, name="student_specific_lesson"),
    path("lessons/<int:lesson_id>/submit_homework", views.submit_homework, name="submit_homework"),
]
