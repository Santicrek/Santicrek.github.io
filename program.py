from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse
from . import views

def index(request):
    return HttpResponse("Hello!")

