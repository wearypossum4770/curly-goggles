from django.db.models import (
	Model, OneToOneField, CharField, DateField,
	BooleanField, ImageField, ForeignKey,
	Q, CASCADE, TextField,DateTimeField,TextChoices,
)
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.crypto import get_random_string
from datetime import datetime
# ~ from core.models import validate_phone_number

# ~ class AddressInformation():
	# ~ class AddressType():
		# ~ MAILING
		# ~ BUSINESS
		# ~ RESIDENTIAL
	# ~ address_type = CharField(max_length = 1, choices =AddressType.choices) 
	# ~ addressed_to = CharField(max_length=50, null=True, blank=True)
	# ~ addressed_care_of = CharField(max_length=50, null=True, blank=True)	
	# ~ address_street_1 = CharField(max_length=50, null=True, blank=True)
	# ~ address_street_2 = CharField(max_length=50, null=True, blank=True)
	# ~ address_city  = CharField(max_length=50, null=True, blank=True)
	# ~ address_state = CharField(max_length=50, null=True, blank=True)
	# ~ address_zip_code = CharField(max_length=50, null=True, blank=True)
	# ~ address_country = CharField(max_length=50, null=True, blank=True)	
	# ~ date_created = DateTimeField(auto_now_add=True)
	# ~ date_modified = DateTimeField(auto_now=True)

class Profile(Model):
	class Rating(TextChoices):
		VERY_POOR=1, _('Very Poor - Required to pay a fee or deposit')
		FAIR=2, _('Fair - Subprime borrower, require higher down payment')
		GOOD=3, _('Good - Offer unfavorable terms (i.e. low down-payment)')
		VERY_GOOD=4, _('Very Good - Offer favorable terms on credit accounts')
		EXCEPTIONAL=5, _('Exceptional - Top of the list offer the best rates')
		__empty__ = _('Unknown - (No Data Avaiable from any source)')
	user = OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)
	mobile_number = CharField(max_length=12, blank=True)
	middle_name = CharField(max_length=30, blank=True)
	birth_date = DateField(null=True)
	client_bio = CharField(max_length=1000, blank=True)
	mobile_validated = BooleanField(default=False)
	email_validated = BooleanField(default=False)
	profile_pic = ImageField(upload_to='user_uploads/profile_pictures/', null=True, blank=True)
	avatar = ImageField(upload_to='user_uploads/avatar/', null=True, blank=True)
	user_timezone = CharField(max_length=50, blank=True)
	client_rating = CharField(max_length=1, choices = Rating.choices, default=Rating.__empty__)
	client_token = CharField(max_length=52, default=get_random_string(50))

	organization = CharField(max_length=50, null=True, blank=True)



	date_created = DateTimeField(auto_now_add=True)
	date_modified = DateTimeField(auto_now=True)


	def __str__(self):
		return self.user.get_fullname()

	def save(self, *args, **kwargs):
		"""
		1. change thumbnails of images.
		2. convert images to webp format
		3. conversion can be done in celery.
		4. send raw image upload to cloud storage api. (protection)
		"""
		super().save(*args, **kwargs)
		profile_img = Image.open(self.profile_pic.path)
		avatar_img = Image.open(self.avatar.path)
		if profile_img.height > 300 or img.width > 300:
			output_size = (300, 300)
			profile_img.thumbnail(output_size)
			profile_img.save(self.image.path)
		if avatar_img.height > 300 or img.width > 300:
			output_size = (300, 300)
			avatar_img.thumbnail(output_size)
			avatar_img.save(self.image.path)
