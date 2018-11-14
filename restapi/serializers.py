from django.contrib.auth.models import User, Group
from rest_framework import serializers

from apps.accounts.models import *
from apps.album.models import *
from apps.comment.models import *
from apps.notification.models import *
from apps.post.models import *
from apps.tag.models import *

# accout
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
# ablum
class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'user_id')


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'key', 'album_id', 'ts', 'desc')
# comment
class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'comment_object_type', 'comment_object_id', 'comment_author')
# post
class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'post_author', 'post_ts',  'post_content','post_title',)
# tag
class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'tag', 'add_ts',  'cover',)
