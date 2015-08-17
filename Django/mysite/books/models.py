#coding=utf-8
from django.db import models


###########################################################
'''增加额外的Manager方法'''
class BookManager(models.Manager):
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()


'''修改初始manager Queryset'''
class DahlBookManager(models.Manager):
    def get_query_set(self):
        return super(DahlBookManager, self).get_query_set().filter(title='World of Plainness')

class MaleManager(models.Manager):
    def get_query_set(self):
        return super(MaleManager, self).get_query_set().filter(sex='M')

class FemaleManager(models.Manager):
    def get_query_set(self):
        return super(FemaleManager, self).get_query_set().filter(sex='F')


########################################################
'''定义数据库表'''
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
    sex = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    people = models.Manager()
    men = MaleManager()
    women = FemaleManager()
    def __unicode__(self):
        return u'%s %s' %(self.first_name, self.last_name)



class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateTimeField(blank=True,null=True)
    num_pages = models.IntegerField(blank=True, null=True)
    objects = BookManager()
    dahl_objects=DahlBookManager()


    def __unicode__(self):
        return self.title