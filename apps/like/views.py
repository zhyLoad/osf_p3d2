from django.shortcuts import render
from apps.notification.models import *
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from apps.accounts.models import MyProfile
from apps.tag.models import Tag
from apps.post.models import Post
from apps.album.models import Album,Photo
from apps.notification.models import *
from apps.comment.models import Comment
from apps.like.models import *
from apps.spost.models import *
import json

# Create your views here.
def dolike(request):
    if request.method == 'POST':
        try:
            author = request.POST['author']
        except:
            author = request.user.id
        object_type = int(request.POST['object_type'])
        object_id = request.POST['object_id']
        like,created = Like.objects.get_or_create(user_id=author,object_type = object_type,object_id = object_id)
        like.save()
        object_title = 0
        if object_type == Dic.OBJECT_TYPE_POST:
            object_title = Post.objects.get(pk=object_id).title
        if object_type == Dic.OBJECT_TYPE_ALBUM:
            object_title = Album.objects.get(pk=object_id).album_title
        if object_type == Dic.OBJECT_TYPE_SHORTPOST:
            object_title = ShortPost.objects.get(pk=object_id).content
        Notification.objects.create(notify_type = Dic.NOTIFY_TYPE_LIKE,
                                     notify_id=0,
                                     object_type=object_type,
                                     object_id=object_id,
                                     notified_user=author,
                                     notifier=request.user.id,
                                    notifier_name =request.user.username,
                                    notifier_avatar =request.user.get_profile().get_mugshot_url(),
                                    object_title = object_title)
        mydict = {"status":"113000"}
        return HttpResponse(json.dumps(mydict),content_type="application/json")
def undolike(request):
    if request.method == 'POST':
        author = request.POST['author']
        object_type = request.POST['object_type']
        object_id = request.POST['object_id']
        like,created = get_object_or_404(Like, user_id=author,object_type = object_type,object_id = object_id)
        like.delete()
        mydict = {"status":"113001"}
        return HttpResponse(json.dumps(mydict),content_type="application/json")