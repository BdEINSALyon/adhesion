from django.conf.urls import include,url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.students),
]

"""from django.conf.urls import url

from . import views

app_name = 'membresva'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]"""