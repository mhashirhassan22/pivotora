from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *



class MessageAdmin(admin.ModelAdmin):
    list_display = ('name','email','message','resolved','sent_at')
    list_editable = ('resolved',)

class EventAdmin(admin.ModelAdmin):
    list_display = ('email','date','start_time','end_time','approved')
    list_editable = ('approved',)




admin.site.register(Event,EventAdmin)
admin.site.register(Message, MessageAdmin)