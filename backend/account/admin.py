from django.contrib import admin
from .models import Course, Student, Faculty, Job, Comment

# class UserAdmin(admin.ModelAdmin):
#     fields = ['username']

# Register your models here.
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Job)
admin.site.register(Comment)