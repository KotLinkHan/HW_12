
from django.contrib import admin
from django.urls import path, include # <--- ВАЖЛИВО: імпорт з django.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("common.urls")),
    path("student/", include("student.urls")),
    path("teacher/", include("teacher.urls")),
    path("parents/", include("parents.urls")),
]