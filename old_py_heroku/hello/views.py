from django.shortcuts import render
from django.http import HttpResponse

from hello.models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

def google_verify(request):
	
	# ~ return HttpResponse (request, "google-site-verification: google0e12d85f2657ecfe.html")
	return render (request, "google0e12d85f2657ecfe.html")

def return_microsoft_spreadsheet():
	response = HttpResponse(my_data, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = 'attachment; filename="foo.xls"'
