from django.urls import path
from chat.views import ThreadView, InboxView

# ~ app_name = 'chat'
urlpatterns = [
    path("", InboxView.as_view()),
    path("<username>/", ThreadView.as_view()),
        # ~ re_path(r"^(?P<username>[\w.@+-]+)", ThreadView.as_view()),

]
