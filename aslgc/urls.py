from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from library.views import *
urlpatterns = patterns('',
	# (r'^accounts/login/$', 'django.contrib.auth.views.login', {'login': 'library/login.html'}),
	url(r'^$',loginpage),
	url(r'^mlogin/',mlogin),
	url(r'^mhome/',mhome),
	url(r'^login/',login_check),
	url(r'^home/',home),
	url(r'^euser/',euser),
	url(r'^ebook/',ebook),
	url(r'^issue/',issue),
	url(r'^issued/',issued),
	url(r'^bookdetails/',bookdetails),
	url(r'^stockdetails/',stockdetails),
	url(r'^stocks/',stocks),
	url(r'^bookreturn/',bookreturn),
	url(r'^bookreturns/',bookreturns),
	url(r'^returns/',returns),
	url(r'^stock/',stock),
	url(r'^user/',userd),
	url(r'^uhistory/',uhistory),
	url(r'^bhistory/',bhistory),
	url(r'^userdetails/',userdetails),
	url(r'^uedit/',uedit),
	url(r'^modify/',modify),
	url(r'^delete/',delete),
	url(r'^bdelete/',bdelete),
	url(r'^bedit/',bedit),
	url(r'^udelete/',udelete),
	url(r'^logout/',logout_view),

	
	
	

	
	
	
	
	
    # Examples:
    # url(r'^$', 'aslgc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
