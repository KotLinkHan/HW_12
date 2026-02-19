from django.shortcuts import render
from django.http import HttpResponse

def student_page(request):
    return HttpResponse("ok student_page")

def student_lesson(request):
    return HttpResponse("ok student_lessons")

def student_specific_lesson(request, lesson_id):
    return HttpResponse(f"ok lesson {lesson_id}")

def submit_homework(request, lesson_id):
    return HttpResponse(f"ok submit_homework for {lesson_id}")