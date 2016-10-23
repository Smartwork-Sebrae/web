from django.conf.urls import url

from history import views

urlpatterns = [
    url(regex=r'^$',
        view=views.DashboardView.as_view(),
        name='dashboard'),
]
