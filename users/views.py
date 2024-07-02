from django.shortcuts import render

# Create your views here.
def ilogin(request):
    return render (request, 'users/login.html')

def iregister(request):
    return render(request, 'users/register.html')