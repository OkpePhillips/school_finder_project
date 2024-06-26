# Generated by Django 4.2.11 on 2024-04-02 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sch_finder_api', '0012_alter_user_middle_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Country Name')),
            ],
        ),
        migrations.RenameField(
            model_name='scholarship',
            old_name='benefit',
            new_name='money',
        ),
        migrations.RemoveField(
            model_name='school',
            name='money',
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sch_finder_api.school', verbose_name='School'),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='City Name')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='sch_finder_api.country')),
            ],
        ),
        migrations.AlterField(
            model_name='school',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sch_finder_api.city'),
        ),
        migrations.AlterField(
            model_name='school',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sch_finder_api.country'),
        ),
    ]
