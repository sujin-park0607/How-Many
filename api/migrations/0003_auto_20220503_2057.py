# Generated by Django 3.1.3 on 2022-05-03 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220502_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='api_id',
            field=models.TextField(),
        ),
    ]
