from django.conf.urls import url
from nrscnetra import views 


app_name = 'netra'
urlpatterns = [
    url(r'^systemregister/$', views.SystemCreate.as_view(), name='systemregister'),
    url(r'^systemlist/$', views.SystemList.as_view(), name='systemlist'),
    url(r'^systemdetail/(?P<pk>\d+)/$', views.SystemDetail.as_view(), name='systemdetail'),
    url(r'^systemupdate/(?P<pk>\d+)/$', views.SystemUpdate.as_view(), name='systemupdate'),
    url(r'^systemdelete/(?P<pk>\d+)/$', views.SystemDelete.as_view(), name='systemdelete'),
]