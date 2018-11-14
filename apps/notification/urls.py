from django.urls import re_path
from .views import *

urlpatterns = [

                        re_path(r'comment/$', comment),
                        re_path(r'follow/$', follow),
                        re_path(r'like/$', like),
                        re_path(r'system/$', system),

 ]
