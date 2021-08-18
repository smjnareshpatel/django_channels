import json

from .models import UserJsonData
from django.views import View
from django.http import HttpResponse

class LoadJsonToDbView(View):
	def get(self, request, *args, **kwargs):

		json_file = open('/home/autopeepal/django_channels/myproject/myapp/1mb-test_json.json',)

		json_data = json.loads(json_file.read())
		j = 0
		for i in json_data:
			obj = UserJsonData.objects.create(country=i['Country'], indicator=i['Indicator'], value=i['Value'], year=i['Year'])
			j = j + 1

		print('Total Doc', len(json_data), 'Document inserted',j)
		return HttpResponse(request, 'hello')
