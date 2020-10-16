from django.urls import path
from core.views import page_418, public_page


urlpatterns = [
path('418/', page_418, name='teapot'),
path('', public_page),
]
