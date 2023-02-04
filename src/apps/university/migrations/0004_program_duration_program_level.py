# Generated by Django 4.1.3 on 2023-02-04 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0003_alter_program_id_alter_university_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='duration',
            field=models.PositiveIntegerField(default=4, help_text='Duration in years, based on 2 semesters a year with 5 courses each.', verbose_name='Duration'),
        ),
        migrations.AddField(
            model_name='program',
            name='level',
            field=models.CharField(choices=[('CERTIFICATE', 'Certificate'), ('DIPLOMA', 'Diploma'), ('BACHELOR', 'Bachelor'), ('MASTER', 'Master'), ('PHD', 'PhD')], default='BACHELOR', max_length=16, verbose_name='Level'),
        ),
    ]