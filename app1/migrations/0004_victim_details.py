# Generated by Django 3.1.2 on 2020-12-04 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_camp_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='victim_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camp_name', models.CharField(max_length=250)),
                ('victim_name', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=250)),
            ],
        ),
    ]