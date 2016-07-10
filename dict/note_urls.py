from django.conf.urls import *
from dict import views

urlpatterns = [
    url(r'^list/(?P<word_id>\d+)/$', views.noteList),
    # url(r'^(?P<word_id>\d+)/$', views.cet4Item),
    url(r'^addNoteDone/$', views.addNoteDone),
    url(r'^backToWord/(?P<dict_id>\d+)/$', views.backToWord),

    # get category word
    # url(r'^((?P<word_level>[A-Za-z]+)/$)', views.leveled_dict_list),
]
