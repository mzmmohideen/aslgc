from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from library.views import *
urlpatterns = patterns('',
	url(r'^$',login_page),
	url(r'^login/',login),
	url(r'^home/',home),
	url(r'^euser/',euser),
	url(r'^ebook/',ebook),
	url(r'^booklend/',booklend),
	url(r'^stock/',stock),
	url(r'^user/',user),

	
	
	
	
	
    # Examples:
    # url(r'^$', 'aslgc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
