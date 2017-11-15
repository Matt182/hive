from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='profile'),
    url(r'^(?P<person_id>[0-9]+)/$', views.person, name='person'),
    url(r'^members/$', views.members, name='members'),
    url(r'^friends/$', views.friends, name='friends'),
    url(r'^send_friend_request/(?P<person_id>[0-9]+)/$', views.send_friend_request, name='send_friend_request'),
    url(r'^accept_friend_request/(?P<person_id>[0-9]+)/$', views.accept_friend_request, name='accept_friend_request'),
    url(r'^decline_recieved_friend_request/(?P<person_id>[0-9]+)/$', views.decline_recieved_friend_request,
        name='decline_recieved_friend_request'),
    url(r'^decline_sended_friend_request/(?P<person_id>[0-9]+)/$', views.decline_sended_friend_request,
        name='decline_sended_friend_request'),
    url(r'^delete_friend/(?P<person_id>[0-9]+)/$', views.delete_friend, name='delete_friend'),
]
