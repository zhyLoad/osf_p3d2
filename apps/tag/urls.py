from django.urls import re_path
from .views import *

urlpatterns = [
                        re_path(r'^create/$', create_post),
                        re_path(r'^list/$', list_post ),
                        re_path(r'^edit/(?P<id>[^/]+)/$', edit_post),
                        re_path(r'^view/(?P<id>[^/]+)/$', view_post),
]
