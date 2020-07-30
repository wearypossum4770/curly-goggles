from django.db.models import(
 Model, CharField,TextField
)
# ~ from lbworkflow.models import BaseWFObj

class SimpleWorkFlow:
	summary = CharField(max_length=255)
	content = CharField(max_length=255)

	def __str__(self):
		return self.summary
