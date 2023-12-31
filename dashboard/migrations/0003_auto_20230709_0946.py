# Generated by Django 3.2.17 on 2023-07-09 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_file_shared_file'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300)),
                ('parent', models.BigIntegerField(default=None)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.user')),
                ('file_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.file_shared')),
            ],
        ),
    ]
