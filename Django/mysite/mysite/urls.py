from django.conf.urls import patterns, include, url
from mysite.views import display_meta
from books import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
     (r'^display/$',display_meta),
     (r'^search-form/$',views.search_form),
     (r'^search/$', views.search),
     (r'^thanks/$',views.thanks),
     (r'^contact-form',views.contact),

)
