from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^sign_up/', views.sign_up, name='sign_up'),
    url(r'^forget_password/', views.forget_password, name='forget_password')
]