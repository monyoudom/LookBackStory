# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import Permission , User

from django.db import models

class UserProfile(models.Model):
    user = models.ForeignKey(User , default=1)
    user_phone = models.CharField(max_length = 15)
    user_image_profile = models.FileField()
    user_address = models.CharField(max_length = 50)
    def __str__(self):
        return self.user + ' - ' + self.user_phone

class Book(models.Model):
    book_title = models.CharField(max_length = 100)
    book_describe = models.CharField(max_length = 100)
    book_cover  = models.ImageField(upload_to='book_cover',default=1)
    def __str__(self):
        return self.book_title 


class Page(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    page_context = models.CharField(max_length = 1000)
    page_num = models.IntegerField(max_length= None)
    def __str__(self):
        return self.page_context 

class UserBook(models.Model):
    user = models.ForeignKey(User, default=1)
    book_title = models.CharField(max_length = 100)
    book_describe = models.CharField(max_length = 200)
    def __str__(self):
        return self.book_title

class UserBookPage(models.Model):
    user_book = models.ForeignKey(UserBook,on_delete=models.CASCADE)
    user_book_page_cotent = models.CharField(max_length=1000)
    user_book_page_num = models.IntegerField(max_length=None)
    def __str__(self):
        return "user_book_page_cotent"+"_"+self.user_book_page_num
    

class PageContent(models.Model):
    page_content = models.ForeignKey(Page,on_delete=models.CASCADE)
    page_content_image = models.ImageField(blank = True,upload_to='page_content_image')
    page_content_audio = models.FileField(blank = True)
    def __str__(self):
        return " page_content"

class PageContentUser(models.Model):
    page_content_user = models.ForeignKey(UserBookPage,on_delete=models.CASCADE)
    page_content_image_user = models.ImageField(blank = True)
    page_content_audio_user = models.FileField(blank = True)
    def __str__(self):
        return self.page_content_user


 
    


    




