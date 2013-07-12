from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'digiqom.appstore.views.home_page'),
    url(r'^appstore/(?P<appId>(\d+))/$', 'digiqom.appstore.views.app_description', name='app_description'),
    url(r'^userinfo/(?P<appId>(\d+))/$', 'digiqom.appstore.views.submit_userinfo',name='submit_user'),
#     url(r'^appstore/', include('digiqom.appstore.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns("django.views",
        url(r'^media(?P<path>.*)/$',
            "static.serve", {
            "document_root": settings.MEDIA_ROOT,
        })
    )