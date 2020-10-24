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
    title = models.CharField(max_length=1200, unique=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    abstract = models.TextField(max_length=10000, null=False)

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

    json_details_es = models.TextField(default=None, null=True)
    json_details_en = models.TextField(default=None, null=True)
    json_files = models.TextField(default=None, null=True)

    def load_details_es(self):
        if self.json_details_es:
            import json
            return json.loads(self.json_details_es)
        return None

    def load_details_en(self):
        if self.json_details_en:
            import json
            return json.loads(self.json_details_en)
        return None

    def load_files(self):
        if self.json_files:
            import json
            return json.loads(self.json_files)
        return None

    def load_title(self):
        if self.title:
            import json
            loads = self.title
            try:
                loads = json.loads(self.title)
            except:
                pass
            print(loads)
            return loads
        return None

    def load_abstract(self):
        if self.abstract:
            import json
            loads = self.abstract
            try:
                loads = json.loads(self.abstract)
            except:
                pass
            print(loads)
            return loads
        return None


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
