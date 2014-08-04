from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',url(r'^$', 'RyadEssalihine.views.home_frontend'),
                          url(r'^welcome$', 'RyadEssalihine.views.welcome'),
                          url(r'^login$', 'RyadEssalihine.views.logine'),
                          url(r'^logout$', 'RyadEssalihine.views.logoute'),
                          url(r'^(?P<username>[0-9a-zA-Z_-]+)/$','RyadEssalihine.views.home_backend'),
                          url(r'^status/', include('status_manager.urls')),              
	                      url(r'^user/', include('user_manager.urls')),
	                      url(r'^calendar/', include('calendar_manager.urls')),
	                      
    # Examples:
    # url(r'^$', 'RyadEssalihine.views.home', name='home'),
    # url(r'^RyadEssalihine/', include('RyadEssalihine.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
