from django.conf.urls import url

from history import views

urlpatterns = [
    url(regex=r'^history/start/$',
        view=views.HistoryApiStart.as_view(),
        name='api_history_start'),
    url(regex=r'^history/finish/$',
        view=views.HistoryApiFinish.as_view(),
        name='api_history_finish'),
]
