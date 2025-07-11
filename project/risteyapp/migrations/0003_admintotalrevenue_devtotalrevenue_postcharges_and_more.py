# Generated by Django 4.2.10 on 2025-03-28 15:31

import django.contrib.auth.validators
from django.db import migrations, models
import risteyapp.utils


class Migration(migrations.Migration):

    dependencies = [
        ('risteyapp', '0002_user_aadhar_user_address_user_age_user_brother_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminTotalRevenue',
            fields=[
                ('id', models.CharField(default=risteyapp.utils.secure_short_uuid, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('month', models.DateField(blank=True, null=True)),
                ('revenue', models.IntegerField(blank=True, null=True)),
                ('user', models.JSONField(blank=True, default=list, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DevTotalRevenue',
            fields=[
                ('id', models.CharField(default=risteyapp.utils.secure_short_uuid, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('month', models.DateField(blank=True, null=True)),
                ('revenue', models.IntegerField(blank=True, null=True)),
                ('user', models.JSONField(blank=True, default=list, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostCharges',
            fields=[
                ('id', models.CharField(default=risteyapp.utils.secure_short_uuid, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('post_charges', models.IntegerField()),
                ('staff_commission', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StaffTotalRevenue',
            fields=[
                ('id', models.CharField(default=risteyapp.utils.secure_short_uuid, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('month', models.DateField(blank=True, null=True)),
                ('revenue', models.IntegerField(blank=True, null=True)),
                ('user', models.JSONField(blank=True, default=list, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StaffTransactions',
            fields=[
                ('id', models.CharField(default=risteyapp.utils.secure_short_uuid, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('staff_id', models.CharField(max_length=25)),
                ('amount', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
                ('type', models.CharField(max_length=10)),
                ('status', models.CharField(default='pending', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='UserImages',
            fields=[
                ('id', models.CharField(default=risteyapp.utils.secure_short_uuid, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(blank=True)),
                ('images', models.ImageField(blank=True, upload_to='User_images')),
            ],
        ),
        migrations.CreateModel(
            name='UserTransactions',
            fields=[
                ('id', models.CharField(default=risteyapp.utils.secure_short_uuid, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('User_id', models.CharField(max_length=25)),
                ('amount', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
                ('type', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
