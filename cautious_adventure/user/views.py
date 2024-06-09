from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CustomUserForm, ProfileForm, LoginForm

# Create your views here.

@login_required
def user_profile(request):
    """profile page"""
    user = request.user
    profile = user.profile
    context = {'profile': profile}
    return render(request, 'user/profile.html', context)


@login_required
def profile_update(request):
    """update profile information"""
    user = request.user
    profile = user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {'form': form}
    return render(request, 'user/profile-form.html', context)


def goto_login(request):
    """
    GET : Go to login form page
    POST: 
        1. logged user redirect to profile page
        2. unlogged user authenticates and logs
        3. redirect to profile page
    """
    if request.user.is_authenticated:
        return redirect('profile')
    
    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        if form.is_valid():
            try:
                user = User.objects.get(username=username)
            except:
                messages.info(request, 'User ' + username + ' is not existed!')
                return render(request, 'user/login.html')

            user = authenticate(request, username=username, password=password)
            if user is None:
                messages.error(request, "Sorry, username OR password is wrong.")
            else:
                login(request, user)
                return redirect('profile')
    
    context = {'form': form}
        
    return render(request, 'user/login.html', context)


def register_user(request):
    """register a user"""
    userForm = CustomUserForm()

    if request.method == 'POST':
        userForm = CustomUserForm(request.POST)
        if userForm.is_valid():
            user = userForm.save(commit=False)
            user.username = user.username.strip().lower()
            if user.first_name:
                user.first_name = user.first_name.strip().title()
            if user.last_name:
                user.last_name = user.last_name.strip().title()
            user.save()
            messages.success(request, "user " + user.username + " has registered successfully!")
            # login the user and redirect to profile.html
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "Sorry, commit info could be wrong, please try again later.")

    context = {'user_form': userForm}
    return render(request, 'user/register-form.html', context)


@login_required
def logout_user(request):
    """logout the logged user"""
    if request.method == 'POST':
        logout(request)
        return redirect('topic-page')

    return render(request, 'user/logout.html')