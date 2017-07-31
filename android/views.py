# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee

# Create your views here.

def employees (request):
	e = list(Employee.objects.all().values())
    
	return JsonResponse(e,safe=False)
