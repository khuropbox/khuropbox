from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('post/<int:pk>/', views.detail, name='detail'),
    path('post/new/', views.new, name='new'),
    path('post/<int:pk>/edit/', views.edit, name='edit'),
    url(r'^drafts/$', views.commentlist, name='commentlist'),

    url(r'^post/(?P<pk>\d+)/remove/$', views.remove, name='remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.commentadd, name='commentadd'),
]