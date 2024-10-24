from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [

    path('',views.logged,name='logged'),
    path('home',views.index,name='index'),
    path('logout',views.logoutUser,name='logout'),
    path('sign', views.signed ,name = 'sign' )

]
