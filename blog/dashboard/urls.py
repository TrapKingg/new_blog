from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^dashboard/$', views.home, name='home'),
    url(r'^buttons/$', views.buttons, name='buttons'),
    url(r'^tables/$', views.tables, name='tables'),
    url(r'^profile/$', views.profile, name='profile'),
]
