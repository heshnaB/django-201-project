# Generated by Django 5.0.4 on 2024-04-11 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_profile_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='message',
            new_name='bio',
        ),
    ]