from django.urls import path
from . import views

urlpatterns = [
    path('', views.parents, name="parents"),
    path('student/<int:student_id>', views.parent_student, name="parent_student"),
    path('lessons/<int:lesson_id>', views.studens_lesson_for_parents, name="studens_lesson_for_parents"),
]
