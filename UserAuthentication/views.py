# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from .forms import UserForm
# Create your views here.
def login(request):
    if request.method == "POST":
        print("test")
        username  = request.POST['username']
        password  = request.POST['password']
        user = authenticate(username = username , password = password)
        if user is not None:
            if user.is_active:
               auth_login(request,user)
               return render(request,'UserDashboard/home.html')
            else:
                return render(request,'UserAuthentication/login.html',{'error_message': 'Your account has been disabled'})
        else:
            return render(request,'UserAuthentication/login.html',{'error_message': 'Invalid login'})
    return render(request,'UserAuthentication/login.html')
    # return HttpResponse("Hello world")
def forget_password(request):
    return render(request,'UserAuthentication/forget_password.html')
def sign_up(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return render(request,'UserDashboard/home.html')
            else:
                return HttpResponse("You are done3")

        else:
            return render(request,'UserAuthentication/login.html',{'succes' : 'Now you can login with your username or email'})
    else:
        render(request,'UserAuthentication/sign_up.html')
        
    context = {
        "form": form,
    }
    return render(request,'UserAuthentication/sign_up.html',context)
