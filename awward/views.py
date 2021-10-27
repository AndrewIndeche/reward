from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Profile, Post,Rate

# Create your views here.
def index(request):
    return HttpResponse('Welcome to the Moringa Tribune')

@login_required(login_url='/accounts/login')
def profile(request):

@login_required(login_url='login')
def user_profile(request, username):

@login_required(login_url='login')
def project(request, post):
