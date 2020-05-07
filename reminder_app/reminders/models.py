from django.db import models

# Create your models here.
class Reminder(models.Model):
    reminderId = models.AutoField(primary_key = True, auto_created=True)
    creator = models.CharField(max_length=200)
    body = models.TextField()
    creationTimeStamp = models.DateTimeField(auto_now_add=True)
    dueTimeStamp = models.DateTimeField()

    def __repr__(self):
        return 'Task body: %s; Task due date: %s' % (self.body, self.dueTimeStamp)

    # def __timeRemaining__(self):

