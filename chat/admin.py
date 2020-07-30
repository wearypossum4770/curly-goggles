from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin, TabularInline, site


from chat.models import Thread, ChatMessage

class ChatMessage(TabularInline):
    model = ChatMessage

class ThreadAdmin(ModelAdmin):
    inlines = [ChatMessage]
    class Meta:
        model = Thread 


site.register(Thread, ThreadAdmin)
