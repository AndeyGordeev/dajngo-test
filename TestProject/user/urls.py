from  django.conf.urls import url, include

from user import views

urlpatterns = [
    url(r'^dashboard/$', views.Dashboard.as_view(), name='dashboard'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^signeup/$', views.SignUpView.as_view(), name='signeup'),
    url('^', include('django.contrib.auth.urls')),
]