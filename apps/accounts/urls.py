from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r'^setting/info$', settingInfoPage),
    re_path(r'^setting/avatar$', settingAvatar),
    re_path(r'^setting/security$', settingSecurity),
    re_path(r'^setting/changepw', resetpwdPage),
    re_path(r'^setting/changeavatar', changeavatar),
]
