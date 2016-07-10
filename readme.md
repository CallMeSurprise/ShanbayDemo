---
title: readme
date: 2016-07-09 22:22:58
categories:
tags:
---
# 题目要求
假设你现在想做一个简单的背单词应用，具体提供下面的 4 项功能：

1. 用户可以根据自己的英语水平，例如 四级，六级，雅思，和托福来设置自己背单词的范围；
2. 每个用户可以设置每天背多少单词
3. 用户背单词过程中能够添加笔记， 也可以查看其他用户共享的笔记
4. 用户背单词过程中，可以看到单词，单词的解释和例句。

# 使用说明
1. 开始
使用PyCharm打开程序，然后`run`即可运行程序。
运行程序，在浏览器内输入`http://127.0.0.1:8000/`，进入默认开始页面。然后选择右上角的**登陆**按钮进行登陆。
2. 登陆
此时在`http://127.0.0.1:8000/user/login/`界面，输入正确的用户名和密码方可登陆，错误则继续在此页面重复登陆操作。
用户名和密码分别为root和root。
> 注册：用户可以注册自己的账号密码，成功后会跳转至登录界面。此处未对用户名密码进行约束，请谨慎操作。
3. 选择单词范围和学习数量
登陆成功则进入`http://127.0.0.1:8000/user/options/`页面。
选择四级`tab`，然后输入自己学习的单词数。如5，即可进入下一界面`http://127.0.0.1:8000/cet4/dailylist/`，先预览自己将要学习的5个单词。
点击上方的`开始学习`链接即可进入单个单词学习模式，即`http://127.0.0.1:8000/cet4/5/40001/`页面。
> 点击六级`tab`对应的图片，会直接进入词库内的所有单词的展示页。只做展示，不重复四级`tab`的工作。托福和GRE界面简略未实现。

4. 单词学习和添加笔记
此时我们在`http://127.0.0.1:8000/cet4/5/40001/`页面。
单词学习页面包括单词、释义、例句以及已有的笔记列表。单击**上一个**、**下一个**按钮即可进行单词切换。
用户可以在**创建笔记**`tab`对应的文本框内输入自己的笔记，对该单词添加笔记。
之后会经过一个页面转换，然后单击链接回到之前的但此页面。

以上即为简单的作业使用说明。更详细的逻辑解释在下面会详细介绍。

# 分析
根据题目要求，对需要的业务逻辑整理分析如下图所示：
![扇贝作业-业务流程图][1]

整体业务可以分为用户管理模块、单词模块和用户笔记模块。加上`django`自带的后台管理模块，共计四部分。其中后台管理模块，稍作配置即可实现，不做详细介绍。
下面针对各个模块做单独分析介绍，并说明目前实现的功能。

## 用户管理模块
普通的用户管理模块包括用户注册、登录、退出登录等主要功能，以及忘记密码、第三方登录、绑定手机/邮箱等辅助功能。

完善的用户注册功能应为用户邮箱+密码（或者手机号码+密码）方式，以及邮箱验证、token管理等。此处简单处理，省去了邮箱验证和token，直接简单的让用户能够与数据库中的已有信息匹配成功后即可登录，并进行后续的单词学习操作。

用户注册部分更多的是实现这一功能，未对用户名和密码进行约束。用户注册成功后，目前没有任何提示信息。如果跳转至登录界面，则说明刚刚注册成功，使用之前注册的账号密码登录即可。

### 访问
开启应用程序后，直接访问：
```
http://127.0.0.1:8000/
```
即可进入默认页面，然后选择登陆，输入账号密码分别为`root`和`root`，即可进入后续的单词范围选择和每日学习单词的设置。


## 单词模块
### 词库设置
根据现实场景分析，同一单词在不同难度等级的词库内的释义及例句差别很大，因此，此处选择根据四级、六级等类别的不同设置不同的单词库，也就是每一个单词范围对应一张数据库表。如目前数据库内的CET4、CET6表。
之后的雅思、托福的数据库表结构和处理逻辑与四级类似，因此选择简化处理，不再重复实现。
用户可以根据类别选择自己的单词背诵范围。

### 每日单词数
此处页面部分只在四级部分设置了输入框，允许用户设置自己每天背诵的单词数。六级等逻辑与之类似，不再重复实现。
用户输入自己要学习的单词数，然后单击`开始学习`按钮，即可学习相应数量的单词。
可以通过单击上一个、下一个按钮切换单词。
以及后面将要介绍的笔记部分。

六级部分可**点击图片**进入相应的词库，此处设置为取出数据库内的所有六级单词并做简单展示（此处只有3个单词作为示例）。

托福和GRE部分不再重复实现。

## 用户笔记模块
用户可以查看系统内所有的关于此单词的笔记，同时可以添加自己的笔记。


## 后台管理模块
后台管理部分借助`django`自带的强大功能，结合一些配置即可实现。
可以在运行程序时，通过:
```
http://127.0.0.1:8000/admin/
```
访问，本人配置的管理员用户名和密码分别为`root`、`rootroot`。
此处的单词导入和用户注册功能，可以通过后台管理员身份添加。



  [1]: ./images/%E6%89%87%E8%B4%9D%E4%BD%9C%E4%B8%9A-%E4%B8%9A%E5%8A%A1%E6%B5%81%E7%A8%8B%E5%9B%BE.PNG "扇贝作业-业务流程图.PNG"