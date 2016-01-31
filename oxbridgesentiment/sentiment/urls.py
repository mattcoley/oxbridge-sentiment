from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^update/name=(?P<name>[a-zA-Z]+)$',views.update,name='update')
]
