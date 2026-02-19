from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=200)

class SchoolClass(models.Model):
    start_year = models.IntegerField()
    letter = models.CharField(max_length=1)

class StudentClass(models.Model):
    student = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)

class Contacts(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)

class Lesson(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    lesson_date = models.DateField()
    lesson_name = models.CharField(max_length=200)
    description = models.TextField()
    home_work = models.TextField()
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)