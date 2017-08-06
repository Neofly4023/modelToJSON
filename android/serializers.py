from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Employee
		fields=('last_name','first_name','birth_date','position')