# Generated by Django 2.2 on 2020-05-07 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0003_auto_20200507_1502'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='reminderId',
            new_name='taskId',
        ),
    ]
