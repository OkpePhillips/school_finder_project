# Generated by Django 4.2.11 on 2024-04-03 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sch_finder_api', '0013_country_rename_benefit_scholarship_money_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scholarship',
            old_name='money',
            new_name='bnefit',
        ),
    ]
