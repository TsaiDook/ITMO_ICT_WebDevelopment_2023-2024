from django.urls import path

from .views import *


urlpatterns = [
	path('', Home.as_view(), name='home_url'),
	path('login', UserLogin.as_view(), name='login_url'),
	path('logout', UserLogout.as_view(), name='logout_url'),
	path('register', UserRegister.as_view(), name='register_url'),
	path('profile', UserProfile.as_view(), name='profile_url'),
	path('homeworks', HomeworksList.as_view(), name='homeworks_list_url'),
	path('homework/<str:slug>', HomeworkDetail.as_view(), name='homework_detail_url'),
	path('grades', GradesList.as_view(), name='grades_list_url'),
	path('solutions', SolutionsList.as_view(), name='solutions_list_url'),
	path('solution/<str:slug>', SolutionDetail.as_view(), name='solution_detail_url'),
]
