from django.urls import re_path
from .views import *

urlpatterns = [

    re_path(r'^create$', create_comment),
    re_path(r'^(?P<type>[^/]+)/(?P<id>[^/]+)/$', get_comments),
    re_path(r'^attach/(?P<type>[A-Za-z]+)/(?P<id>[^/]+)/$', get_attachcomments),
    re_path(r'^attach/(?P<type>[A-Za-z]+)/(?P<id>[^/]+)$', get_attachcomments),

 ]
