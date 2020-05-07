from django.shortcuts import render
from reminders.models import Reminder
from django.contrib.auth.decorators import login_required
from django.http import QueryDict
from datetime import datetime

# Create your views here.
def remindersPage(request):
    reminders = Reminder.objects.filter(creator=request.user).order_by('dueTimeStamp')
    remainingTime = []
    for r in reminders:
        remainingTime.append(r.dueTimeStamp.replace(tzinfo=None) - datetime.now().replace(tzinfo=None))
    return render(request, 'reminders.html', {"reminders": zip(reminders, remainingTime), "user": request.user if not request.user.is_anonymous else None})

@login_required(login_url="/login/")
def createTask(request):
    queries = QueryDict(request.body)
    taskBody = queries["taskBody"]
    taskDueDate = queries["reminderDueDate"]
    currentTask = Reminder.objects.create(creator=request.user, body=taskBody, dueTimeStamp=taskDueDate)

    reminders = Reminder.objects.filter(creator=request.user).order_by('dueTimeStamp')
    remainingTime = []
    for r in reminders:
        remainingTime.append(r.dueTimeStamp.replace(tzinfo=None) - datetime.now().replace(tzinfo=None))
    return render(request, 'reminders.html', {"reminders": zip(reminders, remainingTime), "user": request.user if not request.user.is_anonymous else None})

@login_required(login_url="/login/")
def deleteTask(request, reminderId):
    task = Reminder.objects.get(reminderId = reminderId)
    task.delete()
    
    reminders = Reminder.objects.filter(creator=request.user).order_by('dueTimeStamp')
    remainingTime = []
    for r in reminders:
        remainingTime.append(r.dueTimeStamp.replace(tzinfo=None) - datetime.now().replace(tzinfo=None))
    return render(request, 'reminders.html', {"reminders": zip(reminders, remainingTime), "user": request.user if not request.user.is_anonymous else None})
