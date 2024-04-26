# Generated by Django 5.0.4 on 2024-04-26 05:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PANCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/images')),
            ],
        ),
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('DOB', models.DateField(blank=True, max_length=10, null=True)),
                ('Pan', models.CharField(blank=True, max_length=10, null=True)),
                ('Fathers_Name', models.CharField(blank=True, max_length=200, null=True)),
                ('aadhar_gender', models.CharField(blank=True, max_length=10, null=True)),
                ('aadhar_number', models.IntegerField(blank=True, max_length=12, null=True)),
                ('aadhar_Phone', models.PositiveIntegerField(blank=True, max_length=10, null=True)),
                ('aadhar_address', models.TextField(blank=True, null=True)),
                ('pin', models.PositiveIntegerField(blank=True, max_length=6, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
