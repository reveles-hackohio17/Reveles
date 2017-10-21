from django.db import models
from django.utils import timezone

class Event(models.Model):
    author = models.ForeignKey('auth.User')
    event_name = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    cost = models.TextField()
    num_likes = models.IntegerField()
    num_attendees = models.IntegerField()
    thumbnail = models.ImageField()
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.event_name
