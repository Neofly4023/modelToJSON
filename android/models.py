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



class APIClient (models.Model):
	##Token related fields
	access_token = models.CharField(max_length=255,blank=True)
	expires_on = models.DateTimeField(null=True)
	epired = models.BooleanField(default=False)

	##Client related fields
	name = models.CharField(max_length=255)
	key = models.CharField(max_length=255)
	secret = models.CharField(max_length=255)

	def generate_key_and_secret(self):
		""" generates a random key and secret combo """
		key = _createHash()
		secret = _createHash()

		return (key,secret)

	def set_key_and_secret(self,key=None,sec=None):
		""" Associates the given key and sec to the instance 
		of self. If no key and secret were given, they will
		be automaticlally generated """

		nkey,nsec = self.generate_key_and_secret()
		key = key if key else nkey
		sec = sec if sec else nsec

		# Associate key and secret with self
		self.key = key
		self.secret = sec
		self.save()

	def save(self,*args,**kwargs):
		super(APIClient,self).save(*args,**kwargs)
		if not (self.key or self.secret):
			self.set_key_and_secret()
