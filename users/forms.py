from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
	password2
	def clean_data(self):
		return self

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','username', 'password','password2']

class UserUpdateForm(ModelForm):
	
	class Meta:
		model = User
		
class ProfileUpdateForm(ModelForm):
	
	class Meta:
		model = Profile
		fields = '__all__'
