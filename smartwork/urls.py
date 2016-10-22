from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('core.urls', namespace='core')),
    url(r'^orders/', include('order.urls', namespace='order')),
    url(r'^items/', include('item.urls', namespace='item')),
    url(r'^desks/', include('desk.urls', namespace='desk')),
]
