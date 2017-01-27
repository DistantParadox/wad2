from __future__ import unicode_literals
from django.db import models
from django.contrib import admin

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self): # For python 2, use __unicode__ too
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self): # For Python 2, use __unicode__ too
        return self.title

class PageAdmin(admin.ModelAdmin):
    title = models.CharField(max_length=128, unique=True)
    category = models.ForeignKey(Category)
    url = models.URLField()

    list_display = ('title', 'category', 'url')

    def __str__(self): # For Python 2, use __unicode__ too

        return self.title
