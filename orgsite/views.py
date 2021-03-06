from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
from django.db import IntegrityError
from .models import Organization, FAQs, Activity

def home(request):
	orgs = Organization.objects.all().order_by('Org_Name')
	activities = Activity.objects.all().order_by('-when_created')[:6]
	context = {
		'orgs': orgs,
		'activities': activities
	}
	return render(request, 'home.html', context=context)

def render_faqs(request):
	faqs = FAQs.objects.all().order_by('id')
	context = {
		'faqs': faqs
	}
	return render(request, 'faqs.html', context=context)

def render_activities(request):
	activities = Activity.objects.all().order_by('when_created')
	context = {
		'activities': activities
	}
	return render(request, 'activities.html', context=context)

def render_venues(request):
	venues = Activity.objects.exclude(venue=u'')
	context = {
		'venues': venues
	}
	return render(request, 'venues.html', context=context)

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
			return redirect(reverse('profile',  kwargs={'username':request.user.username}))
		else:
			context['error'] = 'Invalid Credentials'
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

def edit_profile_view(request):
	if request.user.is_authenticated is False:
		return redirect('login_view')
	if request.method == 'POST':
		user = Organization.objects.get(user=request.user)
		user.Org_Name = request.POST.get('name')
		user.shortcut = request.POST.get('shortcut')
		user.email = request.POST.get('email')
		user.description = request.POST.get('description')
		user.mission = request.POST.get('mission')
		user.vision = request.POST.get('vision')
		user.contact = request.POST.get('contact')
		user.save()
	return redirect(reverse('profile', kwargs={'username':request.user.username}))

def add_activity_view(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		description = request.POST.get('description')
		try:
			avatar = request.FILES['avatar']
		except MultiValueDictKeyError:
			avatar = None
		activity_object = Activity.objects.create(user=request.user,Activity_Name=name, description=description, avatar=avatar)
		print('Goodbye, cruel world!')
		return redirect('profile',request.user.username)
	return render(request, 'profile.html')

def edit_activity_view(request, activity):
	if request.user.is_authenticated is False:
		return redirect('login_view')
	if request.method == 'POST':
		user = Activity.objects.get(id=activity)
		original = user.avatar
		try:
			user.avatar = request.FILES['avatar']
		except MultiValueDictKeyError:
			user.avatar = original
		user.description = request.POST.get('description')
		user.Activity_Name = request.POST.get('name')
		user.save()
	return redirect(reverse('profile', kwargs={'username':request.user.username}))

def delete_activity_view(request, id):
    if not request.user.is_authenticated:
        return redirect('login_view')
    activity = Activity.objects.get(id=id)
    print(activity.Activity_Name)
    activity.delete()
    return redirect(reverse('profile', kwargs={'username':request.user.username}))