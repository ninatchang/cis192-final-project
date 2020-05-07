from django.db import models
from datetime import datetime
import humanfriendly

''' Model for each reminder task on our todo list '''
class Reminder(models.Model):
    reminderId = models.AutoField(primary_key = True, auto_created=True)
    creator = models.CharField(max_length=200)
    body = models.TextField()
    creationTimeStamp = models.DateTimeField(auto_now_add=True)
    dueTimeStamp = models.DateTimeField()

    ''' String representation of reminder objects '''
    def __repr__(self):
        return 'Task body: %s; Task due date: %s' % (self.body, self.dueTimeStamp)

    ''' Calculate the amount of time remained to complete task
        If there is still time to complete, it returns the amount of time left
        If the task is overdue, it returns a message telling the user to hurry up
        If the task has no due date, it returns a message telling the user that it has no due date
    '''
    def timeRemaining(self):
        if self.dueTimeStamp:
            if self.dueTimeStamp.replace(tzinfo=None) > datetime.now().replace(tzinfo=None):
                return humanfriendly.format_timespan(self.dueTimeStamp.replace(tzinfo=None) - datetime.now().replace(tzinfo=None))
            else: 
                return "It's already due! HURRY UP"
        else:
            return "No set due date! Take your time!!"
