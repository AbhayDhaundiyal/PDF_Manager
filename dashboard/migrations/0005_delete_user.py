# Generated by Django 4.1.10 on 2023-07-09 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "dashboard",
            "0004_file_remove_comments_author_remove_file_shared_file_and_more",
        ),
    ]

    operations = [
        migrations.DeleteModel(
            name="User",
        ),
    ]
