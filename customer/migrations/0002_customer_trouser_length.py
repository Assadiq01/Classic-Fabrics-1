# Generated by Django 4.2.7 on 2023-12-05 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='trouser_length',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]