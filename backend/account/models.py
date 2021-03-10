from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator as Min
from django.contrib.postgres.fields import ArrayField
from datetime import date

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    abbrev = models.CharField(max_length=50)
    grade = models.CharField(max_length=3, default="", blank=True, null=True)
    
    def __repr__(self):
        return "{0} - {1} - {2}".format(self.id, self.name, self.description)

class Comment(models.Model):
    body = models.CharField(max_length=1500)
    commenter = models.ForeignKey('Faculty', on_delete=models.CASCADE, null=True)
    course = models.ManyToManyField('Course', default=0, blank=True)

    def __repr__(self):
        return "{0} - {1} - {2}".format(self.id, self.body)

class Job(models.Model):
    description = models.CharField(max_length=150)
    poster = models.ForeignKey('Faculty', on_delete=models.CASCADE, null=True)
    posted_date = models.DateField(date.today())
    hourly_salary = models.FloatField(max_length=10, default=10, blank=True)
    hours_per_week = models.IntegerField(default=10)
    course_req = models.ManyToManyField(Course, default=0, blank=True)
    applicants = models.ManyToManyField('Student', default=0, blank=True)

    def __repr__(self):
        return "{0} - {1} - {2}".format(self.id, self.description)

class Student(AbstractUser):
    major = models.CharField(max_length=50, default="")
    GPA = models.FloatField(default=0, blank=True, null=True)
    # courses = ArrayField(models.CharField(max_length=50, blank=True))
    # applied_positions = ArrayField(models.CharField(max_length=50, blank=True))
    profile_completeness = models.IntegerField(default=0)
    # taken_class = models.ManyToManyField(Course)
    applied_positions = models.ManyToManyField(Job, default=0, blank=True)
    profile_completeness = models.IntegerField(default=0)
    course_taken = models.ManyToManyField(Course, default=0, blank=True)
    resume_pdf = models.FileField(upload_to='pdf', null=True, blank=True)
    transcript = models.FileField(upload_to='pdf', null=True, blank=True)
    comments_recv = models.ManyToManyField('Comment', default=0, blank=True)
    password = models.CharField(max_length=150, default="")

    def __repr__(self):
        return "{0} - {1} - {2}".format(self.id, self.major, self.GPA)

class Faculty(models.Model):
    department = models.CharField(max_length=50, default="")
    profile_completeness = models.IntegerField(default=0)
    posted_jobs = models.ManyToManyField(Job, blank=True)
    courses_taught = models.ManyToManyField(Course, default=0, blank=True)
    comments_made = models.ManyToManyField('Comment', default=0, blank=True)

    def __repr__(self):
        return "{0} - {1}".format(self.id, self.department)

# class User(AbstractUser):
#     # User Login Information
#     is_student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
#     is_faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True)
#     email = models.EmailField(unique=True)

#     def __repr__(self):
#         return "{0} - {1}".format(self.id, self.email)



# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='student_profile')
#     # user.is_student
#     # major = models.CharField(max_length=50)

#     # def __repr__(self):
#     #     return "{0} - {1}".format(self.name, self.email)

# class Faculty(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='faculty_profile')
#     # department = models.CharField(max_length=50)
    
#     # def __repr__(self):
#     #     return "{0} - {1}".format(self.name, self.email