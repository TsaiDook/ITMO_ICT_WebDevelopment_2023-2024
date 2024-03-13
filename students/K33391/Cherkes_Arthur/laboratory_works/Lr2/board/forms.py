from django import forms

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class StudentForm(forms.Form):
	full_name = forms.CharField(max_length=50)
	full_name.widget.attrs.update({'class': 'form-control'})


class SolutionForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	text.widget.attrs.update({'class': 'form-control'})


class CustomAuthenticationForm(AuthenticationForm):
	username = forms.CharField(
		max_length=254,
		widget=forms.TextInput(attrs={'class': 'form-control'})
	)
	password = forms.CharField(
		widget=forms.PasswordInput(attrs={'class': 'form-control'})
	)


class CustomUserCreationForm(UserCreationForm):
	username = forms.CharField(
		max_length=254,
		widget=forms.TextInput(attrs={'class': 'form-control'})
	)
	password1 = forms.CharField(
		widget=forms.PasswordInput(attrs={'class': 'form-control'})
	)
	password2 = forms.CharField(
		widget=forms.PasswordInput(attrs={'class': 'form-control'})
	)
