"""reminder_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from reminders.views import reminders_page, create_task, deleteTask
from user_management.views import login_view, signup_view, logout_

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', reminders_page, name="reminders_page"),
    path('login/', login_view, name="login_page"),
    path('signup/', signup_view, name='signup_view'),
    path('logout/', logout_, name='logout_'),
    path('createTask/', create_task, name="create_task"),
    path('deleteTask/<int:reminderId>', deleteTask, name="deleteTask"),
]
