from django.shortcuts import render,redirect, get_object_or_404
from . models import myUser
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.http import Http404
# Create your views here.

"""Start of user authentication"""
def iregister(request):
    if request.method == 'POST':
        #take in details from the html / frontend
        username    = request.POST['username'] 
        email       = request.POST['email']
        pass1       = request.POST['pass1']
        pass2       = request.POST['pass2']

        if pass1 != pass2:
            messages.error(request, 'Passwords dont match. Try again')
            return render(request, 'users/register.html')
        
        #check for existing email
        if myUser.objects.filter(email=email).exists():
            messages.error(request,'A user with a siliar email exists. Try another.')
            return render(request, 'users/register.html')
        
        user= myUser.objects.create(
            username = username,
            email    =email,
        )
        user.set_password(pass1)
        user.is_active = True 
        user.save()
        return redirect ('login') #when user creates acc successfully they are redirected to the login page
    
    return render(request, 'users/register.html')


def ilogin(request):
    if request.method == 'POST':
        username    = request.POST['username']
        pass1       = request.POST['pass1']

        try:
            get_object_or_404(myUser, username= username)
            user = authenticate(request, username = username, pass1 = pass1)

            if user is not None:
                login(request,user)
                messages.success(f'Welcome {username}')
                return redirect('tasks:index')
            
            else:
                messages.error(request,'Invalid credentials provided')
        except Http404:
            messages.error(request, f'Account with {username} does not exist. CReate account to continue.')
        return render(request, 'users/login.html', {'username': username})
    else:
        return render (request, 'users/login.html')

def ilogout(request):
    logout(request)
    return redirect( 'login' )
"""End of user authentication"""