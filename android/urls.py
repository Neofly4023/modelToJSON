from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.employees, name='employees'),
    url(r'^$', views.json_request, name='employees'),
]
