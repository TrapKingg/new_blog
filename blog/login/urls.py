from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.register),
    #url(r'^home/$', views.home, name='home'),
    url(r'^register/success/$', views.register_success, name='register_success'),
    url(r'^logout/$', views.logout_page),
]
