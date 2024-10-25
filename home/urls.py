from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [

    path('',views.logged,name='logged'),
    path('home',views.index,name='index'),
    path('logout',views.logoutUser,name='logout'),
    path('sign', views.signed ,name = 'sign' ),
    path('template',views.temple ,name = 'template'),
    path('acad',views.acad ,name = 'acad'),
    path('clubs',views.clubs ,name = 'clubs'),
    path('sports',views.sports ,name = 'sports'),
    path('query',views.queries ,name = 'query')

]
