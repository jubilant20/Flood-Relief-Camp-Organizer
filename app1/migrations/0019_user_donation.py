# Generated by Django 3.1.2 on 2020-12-15 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_camp_organizer_registered_user_registered_volunteer_registered'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
