from django.db import models


class Comment(models.Model):
    oid = models.AutoField(primary_key=True)
    data = models.TextField(blank=False, null=False)
    spider = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = False
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
        managed = False
        db_table = 'USER'


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
        managed = False
        db_table = 'VIDEO'
