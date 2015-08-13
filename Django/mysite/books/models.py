#coding=utf-8
from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30,verbose_name=u'姓')
    last_name = models.CharField(max_length=40,verbose_name=u'名')
    email = models.EmailField(blank=True,verbose_name=u'电子邮件')

    def __unicode__(self):
        return u'%s %s' %(self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateTimeField(blank=True,null=True)

    def __unicode__(self):
        return self.title