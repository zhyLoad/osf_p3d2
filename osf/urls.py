from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from django.urls import path, re_path
admin.autodiscover()

from osf import settings

from filebrowser.sites import site

from osf.views import showHomePage,explore,welcome,get_followers,get_followings,user_index

from django.conf.urls.static import static

urlpatterns = [
                        re_path(r'^admin/filebrowser/', site.urls),
                        re_path( r'^grappelli/', include( 'grappelli.urls' ) ),  # grappelli URLS
                        re_path( r'^admin/', admin.site.urls ),
                        re_path( r'^accounts/', include('userena.urls'),),
                        re_path(r'^account/',include('apps.accounts.urls')),

                        re_path(r'^$', showHomePage),
                        re_path(r'^explore/$', explore),
                        re_path(r'^welcome/$', welcome),
                        re_path( r'^followers$', get_followers),
                        re_path( r'^followings$',get_followings),
                        re_path( r'^user/(?P<id>[^/]+)$',user_index),

    # Examples:
    # url(r'^$', 'depot.views.home', name='home'),
    # url(r'^depot/', include('depot.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

]



urlpatterns += [re_path(r'^post/', include('apps.post.urls')),]
urlpatterns += [re_path(r'^spost/', include('apps.spost.urls')),]
urlpatterns += [re_path(r'^album/', include('apps.album.urls')),]
urlpatterns += [re_path(r'^comment/', include('apps.comment.urls')),]
urlpatterns += [re_path(r'^tag/', include('apps.tag.urls')),]
urlpatterns += [re_path(r'^notifications/', include('apps.notification.urls')),]
urlpatterns += [re_path(r'^like/', include('apps.like.urls')),]
urlpatterns += [re_path(r'^follow/', include('apps.follow.urls'),),]
urlpatterns += [re_path(r'^api/', include('restapi.urls')),]

#urlpatterns += patterns('',url(r'^user/', include('accounts.urls')),)

urlpatterns += staticfiles_urlpatterns()


# if settings.DEBUG:
#     urlpatterns += patterns( '', url( r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT } ),
#     url( r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT} ), )


# urlpatterns += [ re_path(r'^media/(?P<path>.*)$', include('django.views.static.serve', {'document_root': settings.MEDIA_ROOT }) ),
#                 re_path( r'^static/(?P<path>.*)$',include( 'django.views.static.serve', {'document_root':settings.STATIC_ROOT} )), ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
