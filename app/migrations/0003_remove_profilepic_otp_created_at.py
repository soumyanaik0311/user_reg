# Generated by Django 5.0.6 on 2024-08-25 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_profilepic_otp_profilepic_otp_created_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profilepic",
            name="otp_created_at",
        ),
    ]
