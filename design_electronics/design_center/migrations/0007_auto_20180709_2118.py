# Generated by Django 2.0.2 on 2018-07-10 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design_center', '0006_auto_20180709_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dcdc',
            name='design_params',
        ),
        migrations.AddField(
            model_name='dcdc',
            name='design_params',
            field=models.ManyToManyField(to='design_center.DesignParamChoices'),
        ),
    ]
