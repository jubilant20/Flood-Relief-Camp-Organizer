# Generated by Django 3.1.2 on 2020-12-07 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_warning_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement_table',
            name='status',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
