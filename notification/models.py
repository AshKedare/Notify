from django.db import models

# Create your models here.
from django.utils import timezone

class Notification(models.Model):
    bot = models.ImageField(upload_to='notifications/images', default='static/support.png')
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="Nitro Jemson")
    category = models.CharField(max_length = 30,default = '')
    date_time = models.DateTimeField(default=timezone.now)  # Set default value to current time
    description = models.TextField()
    image = models.ImageField(upload_to='notifications/images', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Exam(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50)
    category = models.CharField(max_length = 30,default = '')
    def __str__(self):
        return self.name

class Scrolling_notifications(models.Model):
    Id = models.AutoField(primary_key=True)
    description = models.TextField(max_length= 80)
    def __int__(self):
        return self.Id