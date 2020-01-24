from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'problem_one_app'

urlpatterns = [
    path('',views.index, name='index')
]