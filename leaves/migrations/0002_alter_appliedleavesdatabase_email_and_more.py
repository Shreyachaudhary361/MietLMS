# Generated by Django 4.1.1 on 2023-01-15 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("leaves", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appliedleavesdatabase",
            name="email",
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name="approvedleavesdatabase",
            name="email",
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name="cumulativeleavesdatabase",
            name="email",
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name="delapprovedleavesdatabase",
            name="email",
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name="leavesdatabase",
            name="email",
            field=models.EmailField(max_length=254),
        ),
    ]