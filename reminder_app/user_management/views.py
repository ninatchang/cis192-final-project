from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

''' Load login/signup page and execute user log in operation '''
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
    return render(request, 'login.html', {"user": request.user if not request.user.is_anonymous else None})

''' Execute user sign up operation '''
def signup_view(request):
    user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
    login(request, user)
    return redirect('/')

''' Execute user log out operation '''
def logout_(request):
    logout(request)
    return redirect("/login")

