# coding=utf-8
from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.
class Comment (models.Model):
    id = models.AutoField( primary_key = True )
    object_type = models.IntegerField()
    object_id = models.IntegerField()
    author = models.ForeignKey( User,related_name='author',on_delete=models.CASCADE )
    ts = models.DateTimeField( default = datetime.datetime.now() )
    content = models.TextField()
    parent = models.IntegerField()
    parent_author = models.ForeignKey( User,related_name='parent_author',on_delete=models.CASCADE )

