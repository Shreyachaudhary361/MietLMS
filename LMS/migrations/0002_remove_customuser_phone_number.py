# Generated by Django 4.1.1 on 2023-01-15 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("LMS", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="customuser", name="phone_number",),
    ]
