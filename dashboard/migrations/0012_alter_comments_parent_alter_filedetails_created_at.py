# Generated by Django 4.1.10 on 2023-07-14 13:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0011_remove_comments_user_id_comments_author_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comments",
            name="parent",
            field=models.BigIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name="filedetails",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 14, 13, 51, 18, 720911)
            ),
        ),
    ]
