# Generated by Django 3.2.6 on 2021-08-25 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20210825_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='household',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
