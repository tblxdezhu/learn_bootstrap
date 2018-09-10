#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 07/09/2018 11:28 AM
# @Author  : Zhenxuan Xu
# @File    : urls.py
# @Software: Pycharm professional

from django.conf.urls import include, url
from analyse import views

urlpatterns = [
    url(r'^$', views.analyse),
]
