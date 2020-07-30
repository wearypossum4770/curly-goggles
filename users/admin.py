from django.contrib.admin import (
site, StackedInline, AdminSite,
)
from django.contrib.auth.models import User
from users.models import Profile
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# ~ def change_rating(modeladmin, request, queryset):
    # ~ queryset.update(client_rating = request.user.profile.)
    
# ~ change_rating.short_description = "Mark Selected Products as Excellent"

class ProfileInline(StackedInline):
	model = Profile
	can_delete = False
	verbose_name_plural = "user's profile"
	verbose_name = "profile"
	exclude = [
		'mobile_validated','email_validated','bio','client_token',
	]
	readonly_fields = [
		'birth_date','profile_pic','avatar','user_timezone',
	]
	list_filter=[
		'client_rating',
	]

# ~ @site.register(Profile)
class ProfileAdmin(BaseUserAdmin):
	inlines = [ProfileInline,]
	# ~ list_display = ['email','first_name','last_name', 'username', ]

	fieldsets = (
		(None, {
			'fields': (
				'username','email','password','first_name','last_name',
				)
			}),
		)

site.site_title="Admins" 
site.site_header= "Hudson Sorry 07505 Administration"
site.unregister(User)
site.register(User, ProfileAdmin)
