# Generated by Django 4.2.5 on 2023-09-19 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_item_amount_item_car_item_description_item_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='production_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]