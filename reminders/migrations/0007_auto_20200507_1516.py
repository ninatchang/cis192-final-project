# Generated by Django 2.2 on 2020-05-07 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0006_auto_20200507_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='taskId',
        ),
        migrations.AddField(
            model_name='task',
            name='id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
