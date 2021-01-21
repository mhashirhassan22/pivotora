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
        return f'<a href="{url}"> {self.email} </a>'


class Message(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    message = models.TextField()
    resolved = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)