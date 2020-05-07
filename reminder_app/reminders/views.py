from django.shortcuts import render
from reminders.models import Reminder

# Create your views here.
def reminders_page(request):
    reminders = Reminder.objects.all()
    return render(request, 'reminders.html', {"reminders": reminders, "user": request.user if not request.user.is_anonymous else None})
