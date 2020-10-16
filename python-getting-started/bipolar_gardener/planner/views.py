from pprint import PrettyPrinter
from django.http import JsonResponse
import json
import requests
from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import api_view

pp = PrettyPrinter(indent=4)
# Create your views here.

def weather(latitude,longitude):
	url = f"https://api.weather.gov/points/{latitude},{longitude}"
	header={"Accept":"application/ld+json",'User-Agent':("stephen smith", "wearypossum4770@yahoo.com")}
	resp = requests.get(url)
	return resp.json()

@api_view(['GET', 'POST'])
def home(request):
	if request.method=="POST":
		print('\n\n\n')
		userLatitude=request.data.get('data').get('userLatitude')
		userLongitude=request.data.get('data').get('userLongitude')
		response = weather(userLatitude,userLongitude)
		print(response)
		return JsonResponse(response)

		# data = json.JSONDecoder().raw_decode(request.data)
		# pp.pprint(f"\n\n\n{data}")	
	response = {"hello":"world"}
	return JsonResponse(response)