#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 06/09/2018 5:18 PM
# @Author  : Zhenxuan Xu
# @File    : urls.py
# @Software: Pycharm professional

from django.conf.urls import include, url
from common import views

urlpatterns = [
    url(r'^$', views.login),
    url(r'^login/', views.login),
    url(r'^index/', views.index),

]
