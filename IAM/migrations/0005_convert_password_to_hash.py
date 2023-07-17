from django.db import migrations
from django.contrib.auth.hashers import make_password

def convert_passwords(apps, schema_editor):
    myModel = apps.get_model("IAM", "User")
    for row in myModel.objects.all():
        row.password = make_password(row.password)
        row.save()


class Migration(migrations.Migration):

    dependencies = [
        ('IAM', '0004_alter_user_password'),
    ]

    operations = [
        migrations.RunPython(convert_passwords, reverse_code=migrations.RunPython.noop)
    ]