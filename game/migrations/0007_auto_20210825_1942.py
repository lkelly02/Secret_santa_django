# Generated by Django 3.2.6 on 2021-08-25 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_auto_20210825_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='householdmember',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='householdmember',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
