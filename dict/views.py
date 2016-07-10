# -*- coding: UTF-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from dict.models import CET4, CET6, Note, User
from django.utils import timezone
from django.template import RequestContext
from django import forms


# Create your views here.
# welcome
def index(request):
    return render(request, "index.html")


def options(request):
    return render(request, "options.html")


# cet4 goes here
def cet4List(request):
    dict_list = CET4.objects.all()
    return render(request, "list.html", {'dictList': dict_list})


def cet4Item(request, daily_word_num, word_id):
    nextWord = 40011
    lastWord = 40011
    preWord = 40001
    try:
        word_id = int(word_id)
        daily_word_num = int(daily_word_num)
    except ValueError:
        raise Http404()
    # narrow the range
    if 40001 + daily_word_num >= 40011:
        lastWord = 40011
    else:
        lastWord = 40001 + daily_word_num - 1
    if word_id == lastWord:
        nextWord = word_id
    elif word_id < lastWord:
        nextWord = word_id + 1

    if word_id > 40001:
        preWord = word_id - 1

    try:
        dict_item = CET4.objects.get(word_id=word_id)
        noteListByWord = Note.objects.filter(dict_id=word_id)
    except CET4.DoesNotExist:
        raise Http404

    # print(dict_item)
    return render(request, "words.html",
                  {'dictWord': dict_item, 'noteListByWord': noteListByWord, 'daily_word_num': daily_word_num,
                   'nextWord': nextWord, 'preWord': preWord})


def cet4DailyList(request):
    daily_word_num = 5
    if request.method == 'POST':
        daily_word_num = request.POST['num']
    try:
        daily_word_num = int(daily_word_num)
    except ValueError:
        raise Http404
    daily_dict_list = CET4.objects.all()[:daily_word_num]
    des = "/cet4/" + str(daily_word_num) + "/40001"
    return render(request, "cet4list.html", {'dictList': daily_dict_list, 'des': des})


# cet6 goes here
def cet6List(request):
    dict_list = CET6.objects.all()
    return render(request, "list.html", {'dictList': dict_list})


# def leveled_dict_list(request, word_level):
#     word_level = word_level
#     leveledDictList = Level.objects.filter(word_level=True)
#     return render(request, "notes.html", {'leveledDictList': leveledDictList})


def noteList(request, word_id):
    note_list = Note.objects.filter(dict_id=word_id)
    return render(request, "notes.html", {'note_list': note_list})


def addNoteDone(request):
    add_note = Note()
    if request.method == 'POST':
        content = request.POST['content']
        dict_id = request.POST['word_id']
        daily_word_num = request.POST['daily_word_num']
    add_note.content = content
    add_note.dict_id = dict_id
    add_note.user = User.objects.get(user_id=1)
    add_note.create_time = timezone.now()
    add_note.save()
    return render(request, "success.html",
                  {"daily_word_num": daily_word_num,
                   'dict_id': dict_id})  # , {"note": content}) HttpResponseRedirect('/user/login/')


def backToWord(request, dict_id):
    des = '/cet4/' + dict_id
    return HttpResponseRedirect(des)


# 表单
class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())


# user goes here
# def userLogin(request):
#     return render(request, "login.html")

# 登陆
def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            # 获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 获取的表单数据与数据库进行比较
            user = User.objects.filter(user_name__exact=username, password__exact=password)
            if user:
                # 比较成功，跳转index
                response = HttpResponseRedirect('/user/options/')
                # 将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username', username, 3600)
                return response
            else:
                # 比较失败，还在login
                return HttpResponseRedirect('/user/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html', {'uf': uf}, context_instance=RequestContext(req))


def regist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            # 获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 添加到数据库
            User.objects.create(user_name=username, password=password)
            return HttpResponseRedirect('/user/login/')
    else:
        uf = UserForm()
    return render_to_response('regist.html', {'uf': uf}, context_instance=RequestContext(request))
