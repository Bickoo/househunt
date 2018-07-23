from django.conf.urls import url
from django.contrib import admin

from .views import (
    houses_list,
    houses_create,
    houses_detail,
    houses_update,
    houses_delete,
    )

urlpatterns = [
    url(r'^$', houses_list, name='list'),
    url(r'^create/$', houses_create),
    url(r'^(?P<id>\d+)/$', houses_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', houses_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', houses_delete),
]