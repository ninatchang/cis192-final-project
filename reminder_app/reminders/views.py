from django.shortcuts import render
from reminders.models import Reminder
from django.contrib.auth.decorators import login_required
from django.http import QueryDict

# Create your views here.
def reminders_page(request):
    reminders = Reminder.objects.all()
    return render(request, 'reminders.html', {"reminders": reminders, "user": request.user if not request.user.is_anonymous else None})

@login_required(login_url="/login/")
def create_task(request):
    queries = QueryDict(request.body)
    taskBody = queries["taskBody"]
    taskDueDate = queries["reminderDueDate"]
    currentTask = Reminder.objects.create(creator=request.user, body=taskBody, dueTimeStamp=taskDueDate)

    reminders = Reminder.objects.all()
    return render(request, 'reminders.html', {"reminders": reminders, "user": request.user if not request.user.is_anonymous else None})
