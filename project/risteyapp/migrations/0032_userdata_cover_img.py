# Generated by Django 5.1.1 on 2025-06-11 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risteyapp', '0031_remove_userdata_cover_img_userimages_cover_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='cover_img',
            field=models.ImageField(blank=True, default='User_Pic/profilepic.jpg', null=True, upload_to='User_cover_pic'),
        ),
    ]
