# Generated by Django 4.1.3 on 2023-02-04 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='id',
            field=models.UUIDField(auto_created=True, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='university',
            name='id',
            field=models.UUIDField(auto_created=True, editable=False, primary_key=True, serialize=False),
        ),
    ]
