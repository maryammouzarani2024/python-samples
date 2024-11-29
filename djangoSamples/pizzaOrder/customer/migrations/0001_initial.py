# Generated by Django 5.1.3 on 2024-11-18 08:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pizza', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('post_code', models.CharField(max_length=30)),
                ('phone', models.IntegerField(default=123)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(auto_now=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('extra_topping1', models.CharField(max_length=255)),
                ('extra_topping2', models.CharField(max_length=255)),
                ('other_wishes', models.CharField(max_length=255)),
                ('customer', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('pizza_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.pizza')),
            ],
        ),
    ]