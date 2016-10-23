from django.conf.urls import url

from history import views

urlpatterns = [
    url(regex=r'^history/start/(?P<pk>\d+)/$',
        view=views.HistoryApiStart.as_view(),
        name='api_history_start'),
    url(regex=r'^history/finish/(?P<pk>\d+)/$',
        view=views.HistoryApiFinish.as_view(),
        name='api_history_finish'),
    url(regex=r'^dashboard/$',
        view=views.ApiDashboard.as_view(),
        name='api_dashboard'),
    url(regex=r'^history/dashboard/$',
        view=views.DashboardView.as_view(),
        name='dashboard'),
    url(regex=r'^history/api/order/(?P<pk>\d+)/productivity/$',
        view=views.ApiOrderProductivity.as_view(),
        name='api_history_order_productivity'),
    url(regex=r'^history/order/productivity/$',
        view=views.OrderProductivityView.as_view(),
        name='history_order_productivity'),
]
