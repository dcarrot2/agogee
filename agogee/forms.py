from django import forms
from agogee.models import UserProfile

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PassWordInput())

	class Meta:
		model = UserForm
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('website', 'picture')
