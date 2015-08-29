from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('blogapp.views',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','index',name='index'),
    url(r'^post/(?P<pk>\d+)/$','Post',name='post'),
    url(r"^category/(?P<pk>\d+)/$", "category", name="category"),


)


