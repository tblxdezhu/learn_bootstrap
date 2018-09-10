#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 07/09/2018 11:42 AM
# @Author  : Zhenxuan Xu
# @File    : urls.py
# @Software: Pycharm professional
from django.conf.urls import include, url
from Test import views

urlpatterns = [
    url(r'^$', views.test),
    url(r'test/step2/', views.step2),
]
