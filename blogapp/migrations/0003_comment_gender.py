# Generated by Django 5.0 on 2023-12-14 20:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blogapp", "0002_comment_comment_blogapp_com_created_22385d_idx"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="gender",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female")], default="M", max_length=2
            ),
        ),
    ]