# Generated by Django 2.2.12 on 2020-06-14 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20200614_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postit',
            name='tasks',
        ),
        migrations.AddField(
            model_name='task',
            name='tasks',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.PostIt'),
        ),
    ]
