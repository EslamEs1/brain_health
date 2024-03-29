# Generated by Django 4.1.9 on 2023-05-15 23:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("health", "0006_delete_feedback"),
    ]

    operations = [
        migrations.CreateModel(
            name="SendMail",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("message_text", models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name="suggestion",
            name="from_age",
        ),
        migrations.RemoveField(
            model_name="suggestion",
            name="to_age",
        ),
        migrations.AddField(
            model_name="mood",
            name="img_emoji",
            field=models.ImageField(default="asd", upload_to="mood/emoji"),
            preserve_default=False,
        ),
    ]
