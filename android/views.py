# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets 
from django.shortcuts import render
from django.http import JsonResponse , HttpResponse
from .models import Employee
from .serializers import EmployeeSerializer
import json

# Create your views here.

def employees (request):


	# e = list(Employee.objects.all().values())

	e = Employee.objects.all()
	dictionary = {}
	myList = []

	dictionary = [obj.as_dict() for obj in e]

	"""for v in e:

		dictionary["last_name"]= v.last_name
		dictionary["first_name"]= v.first_name
		dictionary["birth_date"]= v.birth_date
		dictionary["position"]= v.position
		myList.append(dictionary.copy())"""
		
	return HttpResponse(json.dumps(dictionary), content_type='application/json') #JsonResponse(myList,safe=False)



class EmployeeViewSet(viewsets.ModelViewSet):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer