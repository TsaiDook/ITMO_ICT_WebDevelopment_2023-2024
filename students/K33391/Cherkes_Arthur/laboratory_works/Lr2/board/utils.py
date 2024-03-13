from django.http import HttpResponseForbidden

from .models import Student


def student_required(view_func):
	def wrapped_view(request, *args, **kwargs):
		if Student.objects.filter(user=request.user):
			return view_func(request, *args, **kwargs)
		else:
			return HttpResponseForbidden('You need to fill your profile')

	return wrapped_view
