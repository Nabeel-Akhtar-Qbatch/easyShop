# Generated by Django 4.1.7 on 2023-06-06 05:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_alter_cartitem_created_at_alter_category_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 6, 5, 23, 9, 789231)),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 6, 5, 23, 9, 789231)),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 6, 5, 23, 9, 789231)),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 6, 5, 23, 9, 789231)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 6, 5, 23, 9, 789231)),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 6, 5, 23, 9, 789231)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 6, 5, 23, 9, 789231)),
        ),
    ]
