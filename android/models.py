# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Employee ( models.Model ):

	last_name = models.CharField(max_length=30)
	first_name = models.CharField(max_length=30)
	birth_date = models.DateField()
	position = models.CharField(max_length=100)

class User ( models.Model ):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
