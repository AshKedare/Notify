from django.shortcuts import render
from notification.models import Notification,Exam, Scrolling_notifications

# Create your views here.
def index(request):
    # Retrieve all notifications from the database
    notifications = Notification.objects.all()

    # Retrieve all exams from the database
    exams = Exam.objects.all()  

    # Retrieve all exams from the database
    scrolling_notifications = Scrolling_notifications.objects.all()  

     # Pass the notifications to the template context
    context = {
        'notifications': notifications,     
        'exams' : exams,
        'Scrolling' : scrolling_notifications
    }

    # Render the template with the context
    return render(request, 'base.html', context)


