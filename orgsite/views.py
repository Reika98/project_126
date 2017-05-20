from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Organization, FAQs, Activity

def home(request):
    orgs = Organization.objects.all().order_by('Org_Name')
    context = {
        'orgs': orgs
    }
    return render(request, 'home.html', context=context) 

def render_faqs(request):
    faqs = FAQs.objects.all().order_by('id')
    context = {
        'faqs': faqs
    }

    return render(request, 'faqs.html', context=context)

def login_view(request):
	if request.user.is_authenticated:
		return redirect('/')
	context = {}
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			return redirect('home')
		else:
			context['error'] = 'Invalid Username of Password'
			context['username'] = username
	return render(request, 'home.html', context=context)

def logout_view(request):
    logout(request)
    return redirect('home')

def profile_view(request, username):
	orgs = get_object_or_404(User, username=username)
	context = {
		'org': orgs,
		'activity': orgs.activity.all().order_by('-when_created')
    }
	return render(request, 'profile.html', context=context)