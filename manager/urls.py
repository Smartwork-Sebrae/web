from django.conf.urls import url

from manager import views

urlpatterns = [
    url(regex=r'^$',
        view=views.ManagerList.as_view(),
        name='list'),
    url(regex=r'^create/$',
        view=views.ManagerCreate.as_view(),
        name='create'),
    url(regex=r'^(?P<pk>\d+)/$',
        view=views.ManagerDetail.as_view(),
        name='detail'),
    url(regex=r'^(?P<pk>[\w-]+)/update/$',
        view=views.ManagerUpdate.as_view(),
        name='update'),
    url(regex=r'^(?P<pk>[\w-]+)/delete/$',
        view=views.ManagerDelete.as_view(),
        name='delete'),
]
