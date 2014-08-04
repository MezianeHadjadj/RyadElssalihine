from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('user_manager.views',
	                                        url(r'^register$', 'register'),
                                            url(r'^tabs$','tabs_list'),
                                             url(r'^footers$','footers_list'),
                                            #url(r'^apps$','applications'),
                                            #url(r'^pages$','pages'),

	                                        url(r'^users$', 'user_list'),
	                                        url(r'^user/$', 'user_get'),
    # Examples:
    # url(r'^$', 'RyadEssalihine.views.home', name='home'),
    # url(r'^RyadEssalihine/', include('RyadEssalihine.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)