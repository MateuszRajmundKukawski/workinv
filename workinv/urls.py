from django.conf.urls import include, url
from django.contrib import admin
from worktime.views import InventListView


urlpatterns = [
    # Examples:
    # url(r'^$', 'workinv.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^invent/$', InventListView.as_view()),
]
