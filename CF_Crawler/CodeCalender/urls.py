from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.code_calender, name='code_calender'),
    ]