from django.db import models
from common.models import Lesson

class Files(models.Model):
    file_path = models.FileField(upload_to='files/')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

class Grades(models.Model):
    student = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='grades_student')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    teacher = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='grades_teacher')