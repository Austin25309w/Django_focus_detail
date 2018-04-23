from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^validate$', views.validate),
	url(r'^dashboard$', views.dashboard),
	url(r'^logout$', views.logout),
	url(r'^login$', views.login),
	url(r'^delete/(?P<id>\d+)$', views.delete),
	url(r'^add$', views.add),
	url(r'^process$', views.process)






]