from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers


# class Base64ImageField(serializers.ImageField):
#     def to_internal_value(self, data):
#         from django.core.files.base import ContentFile
#         import base64
#         import six
#         import uuid
#
#         if isinstance(data, six.string_types):
#             if 'data:' in data and ';base64,' in data:
#                 header, data = data.split(';base64,')
#
#             try:
#                 decoded_file = base64.b64decode(data)
#             except TypeError:
#                 self.fail('invalid_image')
#
#             file_name = str(uuid.uuid4())[:12]
#             file_extension = self.get_file_extension(file_name, decoded_file)
#             complete_file_name = "%s.%s"%(file_name, file_extension, )
#             data = ContentFile(decoded_file, name=complete_file_name)
#
#             return super(Base64ImageField, self).to_internal_value(data)
#
#     def get_file_extension(self, file_name, decoded_file):
#         import imghdr
#         extension = imghdr.what(file_name, decoded_file)
#         extension = "jpg" if extension == "jpeg" else extension
#         return extension


class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(draf=False).filter(publish_lte=timezone.now())


def upload_location(instance, filename):
    post_model = instance.__class__
    new_id = post_model.objects.order_by("id").last().id + 1

    return "%s/%s" % (new_id, filename)


class Post(models.Model):
    owner = models.ForeignKey(User,
                              related_name="posts",
                              on_delete=models.CASCADE,
                              null=True)
    title = models.CharField(max_length=120, unique=False)
    # perezoso, babosa, haragan
    # slug = models.SlugField(unique=True, null=True)
    # created
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    # body
    context = models.TextField()
    abstract = models.TextField(max_length=1000, null=False)

    image = models.TextField(default=None, null=True)

    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)

    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=True, auto_now_add=False)
    read_time = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    news = models.BooleanField(default=False)
    countLike = models.IntegerField(default=0)
    object = PostManager


class Comment(models.Model):
    owner = models.ForeignKey(User,
                              related_name="comments",
                              on_delete=models.CASCADE,
                              null=True)
    # body
    content = models.TextField(null=False)
    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", null=True, related_name='comment_reply', on_delete=models.CASCADE)
    # created
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        if self.parent:
            return 'Reply to comment #%s on post " %s"' % (self.parent.pk, self.post)
        else:
            return 'Comment #%s on post " %s " ' % (self.pk, self.post.title)
