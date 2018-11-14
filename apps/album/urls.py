from django.urls import re_path
from .views import *

urlpatterns =[

    re_path(r'^create$', create_album),
    re_path(r'^list/$', list_album ),
    re_path(r'^edit/(?P<id>[^/]+)/$', edit_album),
    re_path(r'^view/(?P<id>[^/]+)/$', view_album),

    re_path(r'^upload/$', upload_index),
    re_path(r'^upload/photo$', create_photo),
    re_path(r'^upload/postphoto$', create_postphoto),
    re_path(r'^delete/photo/(?P<photo_id>[^/]+)/$', delete_photo),
    re_path(r'^(?P<album_id>[^/]+)/upload/photo$', create_photo_album),
    re_path(r'^(?P<album_id>[^/]+)/delete/photo/(?P<photo_id>[^/]+)/$', create_photo_album),
    re_path(r'^(?P<id>[^/]+)/photos$', view_album),

]
