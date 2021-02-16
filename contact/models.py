from django.db import models
from django.urls import reverse

class Event(models.Model):
    email = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    approved = models.BooleanField(default=False)


    @property
    def get_html_url(self):
        url = reverse('contact:event_edit', args=(self.id,))
        return f'<a href="{url}"> abc </a>'


class Message(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    message = models.TextField()
    resolved = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)

class WebContent(models.Model):
    about_us = models.TextField()
    mission =  models.TextField()
    email1 = models.TextField()
    email2 = models.TextField()
    speciality_image = models.ImageField(upload_to='',null=True,default='img/abc.jpg', blank=True) 

    @property
    def image_url(self):
        if self.speciality_image and hasattr(self.speciality_image, 'url'):
            return self.speciality_image 

class Portfolio(models.Model):
    title_image = models.ImageField(null=True,default='img/abc.jpg', blank=True)    
    short_description = models.TextField()

    @property
    def image_url(self):
        if self.title_image and hasattr(self.title_image, 'url'):
            return self.title_image