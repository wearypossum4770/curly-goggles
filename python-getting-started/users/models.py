from PIL import Image
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db.models import Model,ManyToManyField, CharField, ForeignKey,DateTimeField,DateField, OneToOneField, BooleanField,CASCADE, ImageField
from core.validators import zipcode_validator, phone_validator

# class Address(Model):
	# address_street_1 = CharField(max_length=50)
	# address_street_2 = CharField(max_length=50, null=True)
	# address_city = CharField(max_length=20)
	# address_state = CharField(max_length=2)
	# address_zipcode = CharField(max_length=10, validators=[RegexValidator(zipcode_validator)])
	# geolocation_longitude = CharField(max_length=10, null=True)
	# geolocation_lattitude = CharField(max_length=10, null=True)

class Profile(Model):
	user = OneToOneField(get_user_model(), on_delete=CASCADE)
	electronic_delivery = BooleanField(default=True)
	date_created = DateTimeField(auto_now_add = True)
	date_modified = DateTimeField(auto_now_add=True)
	# parent_account
	mobile_number = CharField(max_length=12,validators=[RegexValidator(phone_validator)])
	is_active_customer= BooleanField(default=True)
	middle_name = CharField(max_length=50, null=True)
	# primary_address = ManyToManyField(Address)
	profile_picture = ImageField(default='jinteki_shakusetsu.jpg', upload_to='users_profile_pictures')

	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)
		img = Image.open(self.profile_picture.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.profile_picture.path)

# class CustomerAddresses(Model):
	# customer = ForeignKey(Address, on_delete=CASCADE)
	# address = ForeignKey(Customer, on_delete=CASCADE)
	# is_valid = BooleanField(default=False)
	# is_primary = BooleanField(default=True)
	# start_date = DateField(auto_now_add=False, null=True)
	# end_date = DateField(auto_now_add=False, null=True)
