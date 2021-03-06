from django.shortcuts import render, render_to_response
from agogee.forms import UserForm
from agogee.forms import UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponseRedirect
from agogee.models import UserProfile

import jawbone_integration
import requests

# Create your views here.

def index(request):
	UserProfile.objects.all()
	top_spartans = UserProfile.objects.order_by('-ranking')[:5]
	for spartan in top_spartans:
		print spartan
	context = {'top_spartans': top_spartans}
	return render(request, 'agogee/spartanMain.html', context)

def register(request):
	if request.session.test_cookie_worked():
		print ">>>> TEST COOKIE WORKED!"
		request.session.delete_test_cookie()

	else:
		print "Failed test cookie"
	context = RequestContext(request)

	registered = False

	print "test"

	if request.method == 'POST':
		print request.POST
		user_form = UserForm(data = request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user
			profile.ranking = 0

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()

			register = True

			return HttpResponseRedirect('/agogee/thankyou')

		else:
			print user_form.errors, profile_form.errors

	else:
		user_form = UserForm()
		profile_form = UserProfileForm

	return render_to_response(
		'agogee/register.html',
		{'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
		context)




def user_login(request):
	context = RequestContext(request)

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user:

			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/agogee/')

			else:
				return HttpResponse("Your agogee account is disabled.")

		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")

	else:
		return render_to_response('agogee/login.html', {}, context)

@login_required
def user_logout(request):
	logout(request)

	return HttpResponseRedirect('/agogee/')

@login_required
def profile(request):
	
	context = RequestContext(request)
	u = User.objects.get(username=request.user)
	
	try:
		
		up = UserProfile.objects.get(user=u)
	except:
		print "none"
		up = None

	context_dict = {'user':u, 'userprofile':up}
	

    ### integration with jawbone ###

    #hardcode the authorization string
	header = {
        'Authorization': 'Bearer b6_3pfGGwEjLGQwKcc35Ru0-Al13wvvmkdMJNNjUQ0eHD4Ce7f5WhAmKfv_1EyUa8EvaJSumcI0GoYT-V9UbpVECdgRlo_GULMgGZS0EumxrKbZFiOmnmAPChBPDZ5JP'
 	}
 	workout_url = 'https://jawbone.com/nudge/api/users/@me/moves'
	jawbone_data = requests.get(workout_url, headers = header)

	context_dict['active_minutes'] = jawbone_integration.get_active_minutes(jawbone_data)
	context_dict['calories_burned'] = jawbone_integration.get_calories_burned(jawbone_data)

	print "*active minutes", context_dict['active_minutes']
	print "*calories burned", context_dict['calories_burned']

	return render_to_response('agogee/profile.html', context_dict, context)



