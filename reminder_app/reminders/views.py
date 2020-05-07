from django.shortcuts import render, redirect
from reminders.models import Reminder
from django.contrib.auth.decorators import login_required
from django.http import QueryDict
from datetime import datetime
import random
import humanfriendly

# Create your views here.
def remindersPage(request):
    reminders = Reminder.objects.filter(creator=request.user).order_by('dueTimeStamp')
    remainingTime = []
    for r in reminders:
        if r.dueTimeStamp:
            remainingTime.append(humanfriendly.format_timespan(r.dueTimeStamp.replace(tzinfo=None) - datetime.now().replace(tzinfo=None)))
        else:
            remainingTime.append("No set due date! Take your time!!")
    return render(request, 'reminders.html', {"reminders": zip(reminders, remainingTime), "user": request.user if not request.user.is_anonymous else None, "suggestion" : request.session.get("suggestion") if request.session.get("suggestion") else ""})

@login_required(login_url="/login/")
def createTask(request):
    queries = QueryDict(request.body)
    taskBody = queries["taskBody"]
    taskDueDate = queries["reminderDueDate"]

    reminders = Reminder.objects.filter(creator=request.user).order_by('dueTimeStamp')
    return redirect("/")
    
@login_required(login_url="/login/")
def deleteTask(request, reminderId):
    task = Reminder.objects.get(reminderId = reminderId)
    task.delete()
    
    reminders = Reminder.objects.filter(creator=request.user).order_by('dueTimeStamp')
    return redirect("/")

@login_required(login_url="/login/")
def chooseRandom(request):
    reminders = Reminder.objects.filter(creator=request.user).order_by('dueTimeStamp')

    choice = random.randint(0, len(reminders) - 1)
    if (len(reminders) != 0):
        request.session["suggestion"] = reminders[choice].body
    return redirect("/")


