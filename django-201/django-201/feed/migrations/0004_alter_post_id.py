# Generated by Django 5.0.4 on 2024-04-11 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
