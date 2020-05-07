from django.shortcuts import render, redirect
from reminders.models import Reminder
from django.contrib.auth.decorators import login_required
from django.http import QueryDict
import random

''' Load the reminders page with the logged in user's tasks '''
def remindersPage(request):
    reminders = Reminder.objects.filter(creator=request.user).order_by('dueTimeStamp')
    remainingTime = []
    for r in reminders:
        remainingTime.append(r.__timeRemaining__())
    print(reminders)
    return render(request, 'reminders.html', {"reminders": zip(reminders, remainingTime), "user": request.user if not request.user.is_anonymous else None, "suggestion" : request.session.get("suggestion") if request.session.get("suggestion") else ""})

''' Create task for logged in user '''
@login_required(login_url="/login/")
def createTask(request):
    queries = QueryDict(request.body)
    taskBody = queries["taskBody"]
    taskDueDate = queries["reminderDueDate"]
    if (taskDueDate == ''):
        currentTask = Reminder.objects.create(creator=request.user, body=taskBody)
    else:
        currentTask = Reminder.objects.create(creator=request.user, body=taskBody, dueTimeStamp=taskDueDate)
    return redirect("/")

''' Delete task for logged in user when s/he marks it as complete '''
@login_required(login_url="/login/")
def deleteTask(request, reminderId):
    task = Reminder.objects.get(reminderId = reminderId)
    task.delete()
    return redirect("/")

''' Picks a random task to display on webpage '''
@login_required(login_url="/login/")
def chooseRandom(request):
    reminders = Reminder.objects.filter(creator=request.user).order_by('dueTimeStamp')
    choice = random.randint(0, len(reminders) - 1)
    if (len(reminders) != 0):
        request.session["suggestion"] = reminders[choice].body
    return redirect("/")


