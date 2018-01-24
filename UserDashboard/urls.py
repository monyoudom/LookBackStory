from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^view_book_detail/(?P<book_id>[0-9]+)/', views.view_book_detail, name='view_book_detail'),
    url(r'^mystory', views.my_story, name='my_story'),
    url(r'^mydaily', views.my_daily, name='my_daily'),
    url(r'^myfriends', views.my_friends, name='my_friends'),
    url(r'^myblog', views.my_blog, name='my_blog'),
    url(r'^myprofile', views.my_profile, name='my_profile'),
     
    
]