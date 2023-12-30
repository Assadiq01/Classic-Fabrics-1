# Generated by Django 4.2.7 on 2023-12-22 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_alter_customer_amount_paid_alter_customer_balance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='ankle',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='armhole',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='biceps',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='bust',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='freehand',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='lap',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='links',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='neck',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='shirt_length',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='shoulder',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='sleeve',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='stamina',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='waist',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='wrist',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]