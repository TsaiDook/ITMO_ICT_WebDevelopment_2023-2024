from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.utils.decorators import method_decorator

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
from .utils import *


class Home(View):
	def get(self, request):
		return redirect('login_url')


@method_decorator(login_required, name='dispatch')
class HomeworksList(View):
	def get(self, request):
		homeworks = Homework.objects.all()
		return render(request, 'board/homeworks_list.html', {'homeworks': homeworks})


@method_decorator(login_required, name='dispatch')
class HomeworkDetail(View):
	def get(self, request, slug):
		homework = get_object_or_404(Homework, slug=slug)
		return render(request, 'board/homework_detail.html', {'homework': homework})


class UserLogin(View):
	def get(self, request):
		form = CustomAuthenticationForm()
		return render(request, 'board/user_login.html', {'form': form})

	def post(self, request):
		form = CustomAuthenticationForm(request=request, data=request.POST)
		if not form.is_valid():
			return render(request, 'board/user_login.html', {'form': form})
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)
		if not user:
			return render(request, 'board/user_login.html', {'form': form})
		login(request, user)
		return redirect('profile_url')


@method_decorator(login_required, name='dispatch')
class UserLogout(View):
	def get(self, request):
		logout(request)
		return redirect('login_url')


class UserRegister(View):
	def get(self, request):
		form = CustomUserCreationForm()
		return render(request, 'board/user_register.html', {'form': form})

	def post(self, request):
		form = CustomUserCreationForm(data=request.POST)
		if not form.is_valid():
			return render(request, 'board/user_register.html', {'form': form})
		form.save()
		username = form.cleaned_data['username']
		password = form.cleaned_data['password1']
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect('profile_url')


@method_decorator(login_required, name='dispatch')
class UserProfile(View):
	def get(self, request):
		try:
			student = Student.objects.get(user_id=request.user.id)
		except Student.DoesNotExist:
			student = None

		if student:
			form = StudentForm(data={'full_name': student.full_name})
		else:
			form = StudentForm()

		return render(request, 'board/user_profile.html', {'form': form})

	def post(self, request):
		form = StudentForm(data=request.POST)
		if not form.is_valid():
			return render(request, 'board/user_profile.html', {'form': form})

		try:
			student = Student.objects.get(user_id=request.user.id)
		except Student.DoesNotExist:
			student = None

		full_name = form.cleaned_data['full_name']
		if student:
			request.user.student.full_name = full_name
			request.user.student.save()
		else:
			Student(user=request.user, full_name=full_name).save()

		form = StudentForm(data={'full_name': full_name})
		return render(request, 'board/user_profile.html', {'form': form})


@method_decorator(login_required, name='dispatch')
@method_decorator(student_required, name='dispatch')
class SolutionsList(View):
	def get(self, request):
		solutions = Solution.objects.filter(student_id=request.user.student.id).all()
		return render(request, 'board/solutions_list.html', {'solutions': solutions})


@method_decorator(login_required, name='dispatch')
@method_decorator(student_required, name='dispatch')
class SolutionDetail(View):
	def get(self, request, slug):
		homework = get_object_or_404(Homework, slug=slug)

		try:
			solution = Solution.objects.get(student=request.user.student, homework=homework)
		except Solution.DoesNotExist:
			solution = None

		if solution:
			form = SolutionForm(data={'text': solution.text})
		else:
			form = SolutionForm()

		return render(request, 'board/solution_detail.html', {'homework': homework, 'form': form})

	def post(self, request, slug):
		homework = get_object_or_404(Homework, slug=slug)

		form = SolutionForm(request.POST)
		if not form.is_valid():
			return render(request, 'board/solution_detail.html', {'homework': homework, 'form': form})

		try:
			solution = Solution.objects.get(student=request.user.student, homework=homework)
		except Solution.DoesNotExist:
			solution = None

		text = form.cleaned_data['text']
		if solution:
			solution.text = text
			solution.save()
		else:
			Solution(student=request.user.student, homework=homework, text=text).save()

		form = SolutionForm(data={'text': text})
		return render(request, 'board/solution_detail.html', {'homework': homework, 'form': form})


class GradesList(View):
	def get(self, request):
		grades = Grade.objects.all()
		return render(request, 'board/grades_list.html', {'grades': grades})
