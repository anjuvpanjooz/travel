from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages,auth
from django.shortcuts import redirect

# Create your views here.
def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        uname=request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        pwd = request.POST['password']
        pwd1 = request.POST['password1']
        if pwd==pwd1:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"username  taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
                  user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=pwd)
                  user.save();
                  return redirect('login')
        else:
             messages.info(request,"password not matching")
             return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')