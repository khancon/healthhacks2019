# Generated by Django 2.1.7 on 2019-11-02 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20191102_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(default=999),
        ),
    ]
