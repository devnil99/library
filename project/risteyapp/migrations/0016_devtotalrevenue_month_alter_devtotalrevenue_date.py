# Generated by Django 4.2.10 on 2025-05-05 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risteyapp', '0015_rename_dev_id_devtotalrevenue_dev_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='devtotalrevenue',
            name='month',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='devtotalrevenue',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
