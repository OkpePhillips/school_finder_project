# Generated by Django 4.2.11 on 2024-03-31 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sch_finder_api', '0010_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, editable=False, max_digits=2, verbose_name='Rating'),
        ),
    ]
