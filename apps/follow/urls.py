from django.urls import re_path
from .views import *

urlpatterns = [
                        re_path(r'^(?P<id>[^/]+)$', dofollow),
                        re_path(r'^undo/(?P<id>[^/]+)$', undofollow),
 ]
