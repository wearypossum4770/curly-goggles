from django.urls import path
from planner.views import home

urlpatterns = [

	path('', home)
]