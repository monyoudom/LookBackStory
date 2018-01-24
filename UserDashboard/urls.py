from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^view_book_detail/(?P<book_id>[0-9]+)/', views.viewBookDetail, name='view_book_detail'),
    
]