from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
	name = models.CharField(max_length=50)


class Educator(models.Model):
	full_name = models.CharField(max_length=50)


class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	full_name = models.CharField(max_length=50)


class Homework(models.Model):
	slug = models.CharField(max_length=50, unique=True)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
	educator = models.ForeignKey(Educator, on_delete=models.CASCADE)
	published = models.DateTimeField(auto_now_add=True)
	deadline = models.DateTimeField()
	description = models.TextField()
	penalties = models.TextField()


class Solution(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
	published = models.DateTimeField(auto_now_add=True)
	last_update = models.DateTimeField(auto_now=True)
	text = models.TextField()


class Grade(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
	grade = models.IntegerField(choices=[(5, 'Excellent'), (4, 'Good'), (3, 'Descent'), (2, 'Poor')])
