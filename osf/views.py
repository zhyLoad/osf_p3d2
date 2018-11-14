#/usr/bin/python
#coding: utf8
from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.urls import reverse

from django.shortcuts import render,get_object_or_404
from django.views.generic import View
# Create your views here.

from apps.accounts.models import MyProfile
from apps.tag.models import Tag
from apps.post.models import Post
from apps.spost.models import *
from apps.album.models import Album,Photo
from apps.notification.models import Notification
from apps.comment.models import Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from apps.follow.models import  Follow
from apps.notification.models import *
from apps.event.models import *
from osf.settings import qiniu_access_key,qiniu_secret_key,qiniu_bucket_name,qiniu_bucket_domain

@login_required
def showHomePage(request):
    img_base_url = qiniu_bucket_domain
    notifications = get_all_notifications(request.user.id)
    follower = Follow.objects.filter(followee = request.user).count()
    following = Follow.objects.filter(follower = request.user).count()
    spost = ShortPost.objects.filter(author = request.user.id).count()
    counter = {'follower':follower,'following':following,'spost':spost}
    feeds = getFeeds(request.user.id)
    dic = Dic()
    popusers = User.objects.filter(id__gt=0)[0:4]
    poptags = Tag.objects.filter(id__gt=0)[0:4]
    t = get_template( 'index.html' )
    return HttpResponse( t.render(context=locals(),request=request) )
def explore(request):
    notifications = get_all_notifications(request.user.id)
    notifications = get_all_notifications(request.user.id)
    t = get_template( 'explore.html' )
    return HttpResponse( t.render( context=locals(),request=request) )
def welcome(request):
    t = get_template( 'welcome.html' )
    # c = RequestContext( request, locals() )
    return HttpResponse( t.render( context=locals(),request=request) )
@login_required
def get_followings(request):
    notifications = get_all_notifications(request.user.id)
    if request.user.is_authenticated():
        followings = User.objects.filter(followee__follower = request.user)
    t = get_template( 'following.html' )
    return HttpResponse( t.render( context=locals(),request=request) )
@login_required
def get_followers(request):
    notifications = get_all_notifications(request.user.id)
    if request.user.is_authenticated():
        followers = User.objects.filter(follower__followee = request.user)
    t = get_template( 'follower.html' )
    return HttpResponse( t.render(context=locals(),request=request) )

@login_required
def user_index(request,id):
    u =get_object_or_404(User,pk=id)
    albums = Album.objects.filter(user_id=u.id).order_by("-create_ts")
    posts = Post.objects.filter(author=u.id).order_by("-ts")
    sposts = ShortPost.objects.filter(author=u.id).order_by("-ts")
    follow = Follow.objects.filter(followee = u ,follower = request.user).exists()
    notifications = get_all_notifications(request.user.id)
    follower = Follow.objects.filter(followee = u).count()
    following = Follow.objects.filter(follower = u).count()
    spost = ShortPost.objects.filter(author = u.id).count()
    counter = {'follower':follower,'following':following,'spost':spost}

    if request.user.is_authenticated():
        followers = User.objects.filter(follower__followee = u)
    t = get_template( 'user.html' )
    return HttpResponse( t.render(context=locals(),request=request) )
