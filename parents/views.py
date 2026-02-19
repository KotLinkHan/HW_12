# parents/views.py
from django.shortcuts import render
from django.http import HttpResponse

def parents(request):
    return HttpResponse("ok")

def parent_student(request, student_id):
    return HttpResponse(f"ok {student_id}")

def studens_lesson_for_parents(request, lesson_id):
    return HttpResponse(f"ok {lesson_id}")