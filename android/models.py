# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Employee ( models.Model ):

	last_name = models.CharField(max_length=30)
	first_name = models.CharField(max_length=30)
	birth_date = models.DateField()
	position = models.CharField(max_length=100)
	
	def __str__(self):
		return "{} {}".format(self.last_name,self.first_name)

	def as_dict(self):

		return {
			"LastName":self.last_name,
			"FirstName":self.first_name,
			"BDate":self.birth_date.isoformat(),
			"Position":self.position

		}	


class User ( models.Model ):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)