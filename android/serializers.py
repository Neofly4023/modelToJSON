from rest_framework import serializers
from rest_framework.generics import CreateAPIView

from .models import Employee
import django.utils

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Employee
		fields=('last_name','first_name','birth_date','position')


class ClientAccessTokenSerializer(serializers.Serializer):
	def create (self,data):
		key = data.get('key')
		secret = data.get('secret')

		try:
			client = APIClient.objects.get(key=key , secret=secret)
			access_token , expires_on = utils.create_client_access_token( client.key, client.secret)
			data['access_token'] = access_token
			data['expires_on'] = expires_on
		
			return data
		except Exception as err:
			raise serializers.ValidationError(str(err))


##View
class GetClientAccessToken(CreateAPIView):

	authentification_classes = []
	permission_classes = []
	serializer_class = ClientAccessTokenSerializer
