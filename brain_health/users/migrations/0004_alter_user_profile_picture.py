# Generated by Django 4.1.9 on 2023-05-14 10:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_user_phone_number_user_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_picture",
            field=models.ImageField(default=True, upload_to="user_profiles/"),
        ),
    ]
