# Generated by Django 4.1.10 on 2023-07-14 13:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0012_alter_comments_parent_alter_filedetails_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="comments",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 14, 13, 57, 10, 426764)
            ),
        ),
        migrations.AlterField(
            model_name="filedetails",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 14, 13, 57, 10, 426515)
            ),
        ),
    ]