# Generated by Django 4.1.1 on 2022-10-09 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0002_alter_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_photo',
        ),
    ]