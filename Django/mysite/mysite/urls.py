from django.conf.urls import *
from books import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

     (r'^admin/', include(admin.site.urls)),
     (r'^search-form/$',views.search_form),
     (r'^search/$', views.search),
     (r'^thanks/$',views.thanks),
     (r'^contact-form',views.contact),
     # (r'^foo/$', views.foobar_view, {'template_name': 'template1.html'}),
     # (r'^bar/$', views.foobar_view, {'template_name': 'template2.html'}),

)
