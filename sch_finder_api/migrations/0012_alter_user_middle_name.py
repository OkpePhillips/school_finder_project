# Generated by Django 4.2.11 on 2024-04-01 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sch_finder_api', '0011_school_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='middle_name',
            field=models.CharField(max_length=255, null=True, verbose_name='Middle Name'),
        ),
    ]