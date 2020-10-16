from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('messages/', include('postman.urls', namespace='postman', app_name='postman')),


]
