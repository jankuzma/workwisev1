# Generated by Django 4.2.3 on 2023-07-29 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_rename_placed_for_job_listing_jobapplication_job_listing_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeruser',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='employeruser',
            name='surname',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='jobseekeruser',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='jobseekeruser',
            name='surname',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
