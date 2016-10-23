from django.conf.urls import url

from history import views

urlpatterns = [
    url(regex=r'^api/start/(?P<pk>\d+)/$',
        view=views.HistoryApiStart.as_view(),
        name='api_history_start'),
    url(regex=r'^api/finish/(?P<pk>\d+)/$',
        view=views.HistoryApiFinish.as_view(),
        name='api_history_finish'),
    url(regex=r'^api/dashboard/$',
        view=views.ApiDashboard.as_view(),
        name='api_dashboard'),
    url(regex=r'^dashboard/$',
        view=views.DashboardView.as_view(),
        name='dashboard'),
    url(regex=r'^api/order/(?P<pk>\d+)/productivity/$',
        view=views.ApiOrderProductivity.as_view(),
        name='api_history_order_productivity'),
    url(regex=r'^order/productivity/$',
        view=views.OrderProductivityView.as_view(),
        name='history_order_productivity'),
]
