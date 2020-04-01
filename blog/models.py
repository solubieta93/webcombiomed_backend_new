from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType


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
    title = models.CharField(max_length=120, unique=True)
    # perezoso, babosa, haragan
    slug = models.SlugField(unique=True, null=True)
    # created
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    # body
    context = models.TextField()

    image = models.ImageField(
        upload_to=upload_location,
        null=True,
        blank=True,
        width_field="width_field",
        height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)

    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=True, auto_now_add=False)
    read_time = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    news = models.BooleanField(default=False)
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
