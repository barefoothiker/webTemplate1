from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    (r'^$', 'templateApp.views.landing'),

    (r'^templateApp/$', 'templateApp.views.landing'),
    (r'^templateApp/processLanding/$', 'templateApp.views.processLanding'),  

    (r'^templateApp/selectColumns/$', 'templateApp.views.selectColumns'),  

    (r'^templateApp/selectColumnsSubmit/$', 'templateApp.views.selectColumnsSubmit'),  

    (r'^templateApp/handleUpload/$', 'templateApp.views.handleUpload'),  

    #(r'^templateApp/selectParameters/$', 'templateApp.views.selectParameters'),  

    #(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL}),

    #(r'^accounts/', include('registration.urls')),

)

urlpatterns += staticfiles_urlpatterns()

#print str(urlpatterns))

