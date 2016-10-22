from django.shortcuts import render
from django.conf.urls import url

from desk import views

urlpatterns = [
    url(regex=r'^$',
        view=views.DeskList.as_view(),
        name='list'),
    url(regex=r'^create/$',
        view=views.DeskCreate.as_view(),
        name='create'),
    url(regex=r'^(?P<pk>\d+)/$',
        view=views.DeskDetail.as_view(),
        name='detail'),
    url(regex=r'^(?P<pk>[\w-]+)/update/$',
        view=views.DeskUpdate.as_view(),
        name='update'),
    url(regex=r'^(?P<pk>[\w-]+)/delete/$',
        view=views.DeskDelete.as_view(),
        name='delete'),
]
