from django.conf.urls import patterns, include, url
from django.http import HttpResponse
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # homepage:
    url(r'^$', 'TatlockBooks.views.home', name='home'),
    
	url(r'^welcome/', 'TatlockBooks.views.welcome', name='welcome'),
	url(r'^contact/', 'TatlockBooks.views.contact', name='contact'),
	url(r'^about/', 'TatlockBooks.views.about', name='about'),
	
	url(r'^works/(?P<work_id>\w+)/$', 'TatlockBooks.views.workpage', name = 'workpage'),
    url(r'^books/(?P<book_label>\w+)/$', 'TatlockBooks.views.bookpage', name = 'bookpage'),
	url(r'^series/(?P<series_id>\w+)/$', 'TatlockBooks.views.seriespage', name = 'seriespage'),
    url(r'^authors/(?P<author_id>\w+)/$', 'TatlockBooks.views.authorpage', name = 'authorpage'),
    url(r'^publishers/(?P<publisher_id>\w+)/$', 'TatlockBooks.views.publisherpage', name = 'publisherpage'),
    url(r'^translators/(?P<translator_id>\w+)/$', 'TatlockBooks.views.translatorpage', name = 'translatorpage'),
   
    url(r'^authorlist/', 'TatlockBooks.views.authorlist', name = 'authorlist'),
    url(r'^publisherlist/', 'TatlockBooks.views.publisherlist', name = 'publisherlist'),
    url(r'^translatorlist/', 'TatlockBooks.views.translatorlist', name = 'translatorlist'),
    url(r'^worklist/', 'TatlockBooks.views.worklist', name = 'worklist'),
    url(r'^booklist/', 'TatlockBooks.views.booklist', name = 'booklist'),
    url(r'^serieslist/', 'TatlockBooks.views.serieslist', name = 'serieslist'),
    
    url(r'^illustrations/', 'TatlockBooks.views.illustrations', name = 'illustrations'),
    url(r'^marginalia/', 'TatlockBooks.views.marginalia', name = 'marginalia'),
    url(r'^inscriptions/', 'TatlockBooks.views.inscriptions', name = 'inscriptions'),
    url(r'^inserts/', 'TatlockBooks.views.inserts', name = 'inserts'),
    url(r'^backmatter/', 'TatlockBooks.views.backmatter', name = 'backmatter'),
    
    url(r'^search/', 'TatlockBooks.views.search', name = 'search'),
    
    # url(r'^TatlockBooks/', include('TatlockBooks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),   
    
)

