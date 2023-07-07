# Generated by Django 3.1.2 on 2020-12-05 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_requirement_table_requirement_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='camp_details',
            name='accomodation',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='camp_details',
            name='bathroom_no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='camp_details',
            name='camp_type',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='camp_details',
            name='food_arrangements',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]