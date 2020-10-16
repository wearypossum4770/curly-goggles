from django.urls import path, include

from django.contrib import admin

admin.autodiscover()
from hello.views import google_verify


urlpatterns = [
    # ~ path("", hello.views.index, name="index"),
    # ~ path("db/", hello.views.db, name="db"),
    path("google0e12d85f2657ecfe.html", google_verify),
    # ~ path("", include('hello.urls')),
    path("admin/", admin.site.urls),
]
