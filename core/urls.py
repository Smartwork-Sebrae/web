from django.conf.urls import url

from core import views

urlpatterns = [
    url(regex=r'^$',
        view=views.IndexView.as_view(),
        name='index'),
]
