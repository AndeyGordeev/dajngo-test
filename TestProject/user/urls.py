from  django.conf.urls import url, include

from user import views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url('^', include('django.contrib.auth.urls')),
]