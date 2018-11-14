from django.urls import re_path
from .views import *

urlpatterns =[

    re_path(r'do$', dolike),
    re_path(r'undo$', undolike),
 ]
