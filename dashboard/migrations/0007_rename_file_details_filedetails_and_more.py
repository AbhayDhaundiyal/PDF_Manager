# Generated by Django 4.1.10 on 2023-07-13 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0006_file_details_remove_file_file_name_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="File_details",
            new_name="FileDetails",
        ),
        migrations.RenameModel(
            old_name="File_Shared",
            new_name="FileShared",
        ),
    ]
