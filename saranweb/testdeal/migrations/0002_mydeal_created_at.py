# Generated by Django 3.2.6 on 2021-08-28 07:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('testdeal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mydeal',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]