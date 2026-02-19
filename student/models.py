from django.db import models
from common.models import Lesson
from teacher.models import Grades

class StudentHomeWork(models.Model):
    student = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    text_data = models.TextField()
    grade = models.ForeignKey(Grades, on_delete=models.CASCADE)

class LessonVisits(models.Model):
    student = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)