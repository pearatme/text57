# Generated by Django 2.0.7 on 2018-07-08 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_recipient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipient',
            name='timeframe',
        ),
        migrations.AddField(
            model_name='recipient',
            name='groups',
            field=models.CharField(default='stf', max_length=3),
        ),
    ]