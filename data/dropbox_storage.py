from django.conf import settings
from dropbox import Dropbox, files

class DropboxAPI():
	
	def __init__(self):
		self.dropbox_api = Dropbox(settings.DROPBOX_SECRET_API_TOKEN)
		self.USER_DIR
	def file_meta_data(self):
		from dropbox.file_properties import PropertyField
	def users_dropbox_upload(self, request):
		CommitInfo (autorename=True)
		dropbox_api.files_upload
