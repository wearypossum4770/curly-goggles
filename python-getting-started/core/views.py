from django.shortcuts import render
from django.http import HttpResponse


def page_418(request):
	return render (request, "418.html")

def public_page(request):
	return HttpResponse('<h1>HELLO GUEST</h1>')
