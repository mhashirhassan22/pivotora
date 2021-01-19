from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *



class MessageAdmin(admin.ModelAdmin):
    list_display = ('name','email','message','resolved','sent_at')
    list_editable = ('resolved',)




admin.site.register(Event)
admin.site.register(Message, MessageAdmin)