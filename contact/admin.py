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



class WebContentAdmin(admin.ModelAdmin):
    list_display = ('id' ,'about_us', 'mission', 'email1','email2', 'speciality_image')
    list_editable = ('about_us', 'mission', 'email1','email2', 'speciality_image',)
    list_display_links = ('id',)

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_image', 'short_description')
    list_editable = ('title_image', 'short_description',)
    list_display_links = ('id',)




admin.site.register(Event,EventAdmin)
admin.site.register(Message, MessageAdmin)

admin.site.register(WebContent, WebContentAdmin)
admin.site.register(Portfolio, PortfolioAdmin)