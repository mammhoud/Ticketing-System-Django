# Generated by Django 4.0.3 on 2022-04-30 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
