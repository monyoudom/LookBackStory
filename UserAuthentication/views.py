# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'UserAuthentication/login.html')
def forget_password(request):
    return render(request,'UserAuthentication/forget_password.html')
def sign_up(request):
    return render(request,'UserAuthentication/sign_up.html')
