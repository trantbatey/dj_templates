from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.info(request, "Confirmation password does not match password")
            return render(request, 'register.html')

        if User.objects.filter(username=username):
            messages.info(request, "Username already exist")
            return render(request, 'register.html')

        if User.objects.filter(email=email):
            messages.info(request, "Email already registered")
            return render(request, 'register.html')
        
        user = User.objects.create_user(username=username,password=password1,
                                        email=email,first_name=first_name,last_name=last_name)
        user.save()
        auth.login(request, user)
        return redirect("/")

    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        
        if user is None:
            messages.info(request, "Login Failed: Either username or password are incorrect.")
            return redirect('login.html')
        
        auth.login(request, user)
        return redirect("/")

    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect("/")


