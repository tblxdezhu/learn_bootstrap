#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 07/09/2018 10:51 AM
# @Author  : Zhenxuan Xu
# @File    : urls.py
# @Software: Pycharm professional

from django.conf.urls import include, url
from data import views

urlpatterns = [
    url(r'^$', views.data),
]
