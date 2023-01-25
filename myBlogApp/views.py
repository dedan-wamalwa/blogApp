from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request,'index.html',{"posts":posts})