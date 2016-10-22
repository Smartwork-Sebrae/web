from django.shortcuts import render
from django.conf.urls import url

from item import views

urlpatterns = [
    url(regex=r'^$',
        view=views.ItemList.as_view(),
        name='list'),
    url(regex=r'^create/$',
        view=views.ItemCreate.as_view(),
        name='create'),
    url(regex=r'^(?P<pk>\d+)/$',
        view=views.ItemDetail.as_view(),
        name='detail'),
    url(regex=r'^(?P<pk>[\w-]+)/update/$',
        view=views.ItemUpdate.as_view(),
        name='update'),
    url(regex=r'^(?P<pk>[\w-]+)/delete/$',
        view=views.ItemDelete.as_view(),
        name='delete'),
]
