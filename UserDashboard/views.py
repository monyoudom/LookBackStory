# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Book,Page

# Create your views here.

def dashboard(request):
    if not request.user.is_authenticated():

        return render(request,'UserAuthentication/login.html')
    else:
        books = Book.objects.all()
        return render(request,'UserDashboard/home.html',{'books':books})


    
    return render(request,'UserDashboard/home.html')

def view_book_detail(request,book_id):
    print book_id
    pages = Page.objects.filter(pk__in=book_id)
    print pages

    return render(request,'UserDashboard/bookdetail.html',{'pages' : pages})

def my_story(request):
    return render(request,'UserDashboard/mystory.html')
def my_daily(request):
    return render(request,'UserDashboard/mydaily.html')
def my_friends(request):
    return render(request,'UserDashboard/myfriends.html')
def my_blog(request):
    return render(request,'UserDashboard/myblog.html')
def my_profile(request):
    return render(request,'UserDashboard/myprofile.html')




    
