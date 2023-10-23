from datetime import date
import os
from django.db.models.fields import DateTimeField
from django.forms.utils import flatatt
from blog.models import Article
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings

from .form import *
from django.contrib.auth import logout



# Create your views here.

def accueil(request):
    posts = Article.objects.all()[:4]

    popular_posts = sorted(Article.objects.all().filter(is_draft=False), key=lambda a: a.get_hit_count, reverse=True)[:4]

    pubi = Article.objects.all().filter(is_draft=False).order_by('-publish_date')


        
    context = {'posts' : posts, 'popular_posts':popular_posts, 'pubi' : pubi,}

    return render(request, 'index.html', context)



def articles(request, *args,  **kwargs):
        popular_posts = sorted(Article.objects.all().filter(is_draft=False), key=lambda a: a.get_hit_count, reverse=True)[:4]

        context = {'popular_posts':popular_posts,}


        return render(request, 'articles.html', context)







def all_pub(request):
    pub = Article.objects.all().filter(is_draft=False).order_by('-publish_date')
    test = sorted(Article.objects.all().filter(is_draft=False), key=lambda a: a.get_hit_count, reverse=True) 
    context = {'pub' : pub, 'test' : test}
    return render(request, 'actualités.html', context)



def blog_detail(request , slug):
    context = {}
    try:
        blog_obj = Article.objects.filter(slug = slug).first()
        context['blog_obj'] =  blog_obj
    except Exception as e:
        print(e)
    return render(request , 'escalde.html' , context)


def see_blog(request):
    context = {}
    
    try:
        blog_objs = Article.objects.filter(user = request.user, is_draft=False)
        context['blog_objs'] =  blog_objs
    except Exception as e: 
        print(e)

    return render(request , 'publications.html' ,context)


def draft(request):
    context = {}
    
    try:
        blog_objs = Article.objects.filter(user = request.user, is_draft=True)
        context['blog_objs'] =  blog_objs
    except Exception as e: 
        print(e)
    
    print(context)
    return render(request , 'brouillons.html' ,context)

# Create your views here.


def about(request, *args,  **kwargs):
        return render(request, 'about.html')

def error(request, *args,  **kwargs):
        return render(request, '404.html')


def contact(request, *args,  **kwargs):
        return render(request, 'contact.html')

def programme(request, *args,  **kwargs):
        return render(request, 'programme.html')

def service(request, *args,  **kwargs):
        return render(request, 'service.html')

def team(request, *args,  **kwargs):
        return render(request, 'team.html')

def testimonial(request, *args,  **kwargs):
        return render(request, 'testimonial.html')