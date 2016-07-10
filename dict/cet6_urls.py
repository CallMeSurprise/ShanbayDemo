from django.conf.urls import *
from dict import views

urlpatterns = [
    url(r'^list/$', views.cet6List),
    # url(r'^(?P<word_id>\d+)/$', views.cet6Item),
    # url(r'^dailylist/(?P<daily_word_num>\d+)/$', views.cet6DailyList)

    # get category word
    # url(r'^((?P<word_level>[A-Za-z]+)/$)', views.leveled_dict_list),
]