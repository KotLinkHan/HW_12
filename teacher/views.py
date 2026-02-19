from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def teacher_page(request):
    return HttpResponse("ok teacher_page")

def teacher_lessons(request):
    return HttpResponse("ok teacher_lessons")

def specific_lesson(request, lesson_id):
    return HttpResponse(f"ok teacher specific_lesson {lesson_id}")

def absence(request, lesson_id):
    return HttpResponse(f"ok absence for {lesson_id}")

def grade(request, lesson_id):
    return HttpResponse(f"ok grade for {lesson_id}")

def check_student_homework(request, lesson_id, homework_id):
    return HttpResponse(f"ok check homework {homework_id} for lesson {lesson_id}")