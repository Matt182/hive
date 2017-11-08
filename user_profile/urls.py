from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='profile'),
    url(r'members/$', views.members, name='members'),
    url(r'friends/$', views.friends, name='friends'),
]
