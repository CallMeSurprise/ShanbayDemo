# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib import admin


# Create your models here.


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    logo_img = models.CharField(max_length=255,
                                default="http://7xrb5e.com1.z0.glb.clouddn.com/avatar.jpg")
    word_level = models.CharField(max_length=10, default='0')
    daily_word_num = models.IntegerField(null=True)
    user_token = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=50)

    # class WordLevel(models.Model):
    #     WordLevel = (
    #         ('4', 'CET4'),
    #         ('6', 'CET6'),
    #         ('8', 'TOEFL'),
    #         ('10', 'GRE'),
    #     )


# 单词：Id、单词、释义、例句


class CET4(models.Model):
    word_id = models.IntegerField()
    word = models.CharField(max_length=21)
    explanation = models.TextField()
    sentences = models.TextField()


class CET6(models.Model):
    word_id = models.IntegerField()
    word = models.CharField(max_length=20)
    explanation = models.TextField()
    sentences = models.TextField()


# word_levels = models.CharField(max_length=5)


# class Level(models.Model):
#     dict = models.ForeignKey(Dict, null=False)
#     CET4 = models.BooleanField(default=False)
#     CET6 = models.BooleanField(default=False)
#     TOEFL = models.BooleanField(default=False)
#     GRE = models.BooleanField(default=False)


class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=False)
    dict_id = models.IntegerField()
    content = models.TextField()
    create_time = models.DateTimeField()

    class Meta:
        ordering = ['-create_time']


##################################################


class CET4Admin(admin.ModelAdmin):
    list_display = ('word_id', 'word', 'explanation', 'sentences')


class CET6Admin(admin.ModelAdmin):
    list_display = ('word_id', 'word', 'explanation', 'sentences')


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name')


class NoteAdmin(admin.ModelAdmin):
    list_display = ('note_id', 'user_id', 'dict_id', 'content')
