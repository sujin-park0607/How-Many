# Generated by Django 3.1.3 on 2022-05-13 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20220512_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stay',
            name='dateTime',
            field=models.DateTimeField(),
        ),
    ]
