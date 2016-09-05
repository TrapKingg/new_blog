from django.conf.urls import include, url
from django.contrib import admin
from login.views import *
from dashboard.views import *
from index.views import *


urlpatterns = [
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^accounts/login/', 'django.contrib.auth.views.login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('login.urls')),
    url(r'^user/', include('dashboard.urls')),
    url(r'^$', 'index.views.landing_page', name='index'),
    url(r'^cuentas/', include('registration.backends.simple.urls')),
]
