from django.conf.urls import include, url
from django.conf import settings
from django.views.static import serve
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^event_log/data/(?P<dataset>.+).json', views.get_dataset),
    url(r'^event_log/$', views.event_log, name='event_log'),
        #login
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # API Urls
    url(r'api/$', views.EventAPIList.as_view()),
    url(r'api/(?P<pk>[0-9]+)/$', views.EventAPIDetail.as_view()),
    url(r'api/intercom/$', views.IntercomAPIList.as_view()),
    url(r'api/intercom/(?P<pk>[0-9]+)/$', views.IntercomAPIDetail.as_view()),
    url(r'api/door/$', views.DoorAPIList.as_view()),
    url(r'api/door/(?P<pk>[0-9]+)/$', views.DoorAPIDetail.as_view()),
    url(r'api/state/$', views.StateAPIList.as_view()),
    url(r'api/state/(?P<pk>[0-9]+)/$', views.StateAPIDetail.as_view()),
    url(r'api/route/$', views.RouteAPIList.as_view()),
    url(r'api/route/(?P<pk>[0-9]+)/$', views.RouteAPIDetail.as_view()),
    url(r'api/actioncommands/$', views.ActionCommandAPIList.as_view()),
    url(r'api/actioncommands/(?P<pk>[0-9]+)/$', views.ActionCommandAPIDetail.as_view()),
    url(r'api/accesscode/$', views.AccessCodeAPIList.as_view()),
    url(r'api/accesscode/(?P<pk>[0-9]+)/$', views.AccessCodeAPIDetail.as_view()),
    url(r'api/person/$', views.PersonAPIList.as_view()),
    url(r'api/person/(?P<pk>[0-9]+)/$', views.PersonAPIDetail.as_view()),
    url(r'api/location/$', views.ActionCommandAPIList.as_view()),
    url(r'api/location/(?P<pk>[0-9]+)/$', views.ActionCommandAPIDetail.as_view()),
]
#Media file upload
if settings.DEBUG:
  urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
  ]
