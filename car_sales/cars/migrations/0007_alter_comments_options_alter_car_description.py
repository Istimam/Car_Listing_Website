# Generated by Django 5.0.6 on 2024-06-11 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_car_author_car_buyers_alter_car_quantity_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['created']},
        ),
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.TextField(max_length=700),
        ),
    ]
