from .models import Posts
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import  render, get_object_or_404
from django.contrib.auth.decorators import login_required

def signin(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('upassword')

        # Authenticate the user
        user = authenticate(request, username=name, password=password)

        if user is not None:
            # Log in the user
            login(request, user)
            return redirect('/')
        else:
            # Display an error message
            messages.error(request, 'Invalid login credentials. Please try again.')

            # Redirect to the login page
            return redirect('/signin/')

    return render(request, 'blog/base.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists. Please use a different email.')
            return redirect('/signup/')  # Redirect back to the signup page

        # Create a new user
        user = User.objects.create_user(username=name, email=email, password=password)

        # Log in the user
        login(request, user)

        # Redirect to a success page or home page
        return redirect('/signin/')  # Change 'home' to the name of your home page URL pattern

    return render(request, 'blog/signup.html')

@login_required(login_url='/signin/')
def home(request):
    content = {
        'posts':Posts.objects.all()
    }
    return render(request, 'blog/home.html', content)

def detail(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    return render(request, 'blog/detail.html', {'post': post})

def logoutUser(request):
    logout(request)
    return redirect('/signin/')
