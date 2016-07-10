from django.conf.urls import *
from dict import views

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^regist/$', views.regist),
    url(r'^options/$', views.options),
    # url(r'^(?P<word_id>\d+)/$', views.cet4_item),
]
