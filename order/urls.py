from django.shortcuts import render
from django.conf.urls import url

from order import views

urlpatterns = [
    url(regex=r'^$',
        view=views.OrderList.as_view(),
        name='list'),
    url(regex=r'^create/$',
        view=views.OrderCreate.as_view(),
        name='create'),
    url(regex=r'^(?P<pk>\d+)/$',
        view=views.OrderDetail.as_view(),
        name='detail'),
    url(regex=r'^(?P<pk>[\w-]+)/update/$',
        view=views.OrderUpdate.as_view(),
        name='update'),
    url(regex=r'^(?P<pk>[\w-]+)/delete/$',
        view=views.OrderDelete.as_view(),
        name='delete'),
]
