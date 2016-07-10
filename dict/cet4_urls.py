from django.conf.urls import *
from dict import views

urlpatterns = [
    url(r'^list/$', views.cet4List),
    url(r'^(?P<daily_word_num>\d+)/(?P<word_id>\d+)/$', views.cet4Item),
    url(r'^dailylist/$', views.cet4DailyList)
    # url(r'^dailylist/(?P<daily_word_num>\d+)/$', views.cet4DailyList)

    # get category word
    # url(r'^((?P<word_level>[A-Za-z]+)/$)', views.leveled_dict_list),
]
