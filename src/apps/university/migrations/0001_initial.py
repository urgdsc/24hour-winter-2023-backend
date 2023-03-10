# Generated by Django 4.1.3 on 2023-02-04 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('description', models.TextField(blank=True, max_length=1024, null=True, verbose_name='Description')),
                ('location', models.CharField(max_length=256, verbose_name='Location')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Website Address')),
                ('is_verified', models.BooleanField(default=False, help_text='Weather the data is verified by the institution', verbose_name='Is Verified')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last modified')),
            ],
            options={
                'verbose_name': 'University',
                'verbose_name_plural': 'Universities',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, max_length=1024, null=True)),
                ('domestic_annual_tuition', models.PositiveIntegerField(help_text='Average annual tuition based on 5 courses per each semester.', verbose_name='Domestic Annual Tuition')),
                ('international_annual_tuition', models.PositiveIntegerField(help_text='Average annual tuition based on 5 courses per each semester.', verbose_name='International Annual Tuition')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last modified')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programs', to='university.university', verbose_name='University')),
            ],
            options={
                'verbose_name': 'Program',
                'verbose_name_plural': 'Programs',
            },
        ),
    ]
