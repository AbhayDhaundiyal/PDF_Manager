# Generated by Django 4.1.10 on 2023-07-13 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0005_delete_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="File_details",
            fields=[
                ("file_id", models.AutoField(primary_key=True, serialize=False)),
                ("file_name", models.CharField(max_length=50)),
                ("is_public", models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name="file",
            name="file_name",
        ),
        migrations.RemoveField(
            model_name="file_shared",
            name="public",
        ),
        migrations.AddField(
            model_name="file",
            name="file_id",
            field=models.BigIntegerField(default=-1),
        ),
    ]
