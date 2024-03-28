# Generated by Django 4.2.11 on 2024-03-28 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sch_finder_api', '0005_user_middle_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='current_degree',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='nationality',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
