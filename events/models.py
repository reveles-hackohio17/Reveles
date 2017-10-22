from django.db import models
from django.utils import timezone

def return_zero():
    return 0

class Event(models.Model):
    author = models.ForeignKey('auth.User')
    event_name = models.CharField(max_length=200)
    general_category = models.CharField(default='Student Org', max_length=100)
    specific_category = models.CharField(default='Engineering', max_length=100)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    cost = models.FloatField(default=0)
    num_likes = models.IntegerField(default=0)
    num_attendees = models.IntegerField(default=0)
    address = models.CharField(max_length=512)
    image = models.TextField(blank=True, null=True)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.event_name
