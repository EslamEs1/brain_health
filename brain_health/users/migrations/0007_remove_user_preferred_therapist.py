# Generated by Django 4.1.9 on 2023-05-14 22:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_alter_user_name_alter_user_profile_picture"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="preferred_therapist",
        ),
    ]
