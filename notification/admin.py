from django.contrib import admin

# Register your models here.

from .models import Notification,Exam, Scrolling_notifications

admin.site.register(Notification)
admin.site.register(Exam)
admin.site.register(Scrolling_notifications)