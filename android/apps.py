# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class AndroidConfig(AppConfig):
    name = 'android'
    def ready(self):
     import android.signals
