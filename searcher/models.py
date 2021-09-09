from django.db import models
import time
import json


class Comment(models.Model):
    oid = models.AutoField(primary_key=True)
    data = models.TextField(blank=False, null=False)
    spider = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'COMMENT'


class User(models.Model):
    mid = models.AutoField(primary_key=True)
    name = models.TextField(blank=False, null=False)
    sex = models.TextField(blank=False, null=False)
    face = models.TextField(blank=False, null=False)
    sign = models.TextField(blank=False, null=False)
    level = models.IntegerField(blank=False, null=False)
    attention = models.IntegerField(blank=False, null=False)
    fans = models.IntegerField(blank=False, null=False)
    localpic = models.IntegerField(blank=False, null=False)
    spider = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'USER'
        indexes = [
            models.Index(fields=['-fans'], name='fans_idx'),
        ]
        ordering = ['-fans']

    def pic_path(self):
        return 'user_face/{}.{}'.format(self.mid, self.face.split('.')[-1])

    def level_icon(self):
        level_to_font = ['xe6cb', 'xe6cc', 'xe6cd',
                         'xe6ce', 'xe6cf', 'xe6d0', 'xe6d1']
        return level_to_font[self.level]


class Video(models.Model):
    aid = models.AutoField(primary_key=True)
    bvid = models.TextField(blank=False, null=False)
    cid = models.IntegerField(blank=False, null=False)
    pic = models.TextField(blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    desc = models.TextField(blank=False, null=False)
    keywords = models.TextField(blank=False, null=False)
    copyright = models.IntegerField(blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False)
    videos = models.IntegerField(blank=False, null=False)
    pubdate = models.IntegerField(blank=False, null=False)
    view = models.IntegerField(blank=False, null=False)
    danmaku = models.IntegerField(blank=False, null=False)
    like = models.IntegerField(blank=False, null=False)
    coin = models.IntegerField(blank=False, null=False)
    favorite = models.IntegerField(blank=False, null=False)
    share = models.IntegerField(blank=False, null=False)
    reply = models.IntegerField(blank=False, null=False)
    owner = models.IntegerField(blank=False, null=False)
    localpic = models.IntegerField(blank=False, null=False)
    spider = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'VIDEO'
        indexes = [
            models.Index(fields=['-view'], name='view_idx'),
            models.Index(fields=['owner'], name='owner_idx'),
        ]
        ordering = ['-view']

    def pic_path(self):
        return 'video_pic/{}.{}'.format(self.aid, self.pic.split('.')[-1])

    def pub_time(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.pubdate))

    def get_owner(self):
        return User.objects.get(mid=self.owner)

    def get_comments(self):
        return json.loads(Comment.objects.get(oid=self.aid).data)[:5]
