from django.shortcuts import render

# Create your views here.
def reminders_page(request):
    return render(request, 'reminders.html', {})
