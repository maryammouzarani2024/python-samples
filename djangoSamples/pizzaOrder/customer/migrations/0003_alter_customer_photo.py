# Generated by Django 5.1.3 on 2024-11-24 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_photo_alter_customer_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='photo',
            field=models.ImageField(null=True, upload_to='profile_photo/'),
        ),
    ]