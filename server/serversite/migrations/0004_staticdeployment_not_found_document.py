# Generated by Django 2.2.2 on 2019-06-18 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serversite', '0003_auto_20180919_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticdeployment',
            name='not_found_document',
            field=models.TextField(blank=True, null=True),
        ),
    ]
