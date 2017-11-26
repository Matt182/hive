from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='profile'),
    url(r'^(?P<person_id>[0-9]+)/$', views.person, name='person'),
    url(r'^members/$', views.members, name='members'),
    url(r'^friends/$', views.friends, name='friends'),
    url(r'^send_friend_request/$', views.send_friend_request, name='send_friend_request'),
    url(r'^accept_friend_request/$', views.accept_friend_request, name='accept_friend_request'),
    url(r'^decline_received_friend_request/$',
        views.decline_received_friend_request,
        name='decline_received_friend_request'
        ),
    url(r'^decline_send_friend_request/$',
        views.decline_send_friend_request,
        name='decline_send_friend_request'
        ),
    url(r'^delete_friend/$', views.delete_friend, name='delete_friend'),
    url(r'^add_profile_info/$', views.add_profile_info, name='add_profile_info'),
]
