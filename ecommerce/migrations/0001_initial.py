# Generated by Django 4.1.7 on 2023-06-05 14:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 6, 5, 14, 29, 47, 823807))),
                ('updated_at', models.DateTimeField(null=True)),
                ('category_name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=100)),
                ('category_type', models.TextField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 6, 5, 14, 29, 47, 823807))),
                ('updated_at', models.DateTimeField(null=True)),
                ('total_amount', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 6, 5, 14, 29, 47, 823807))),
                ('updated_at', models.DateTimeField(null=True)),
                ('user_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 6, 5, 14, 29, 47, 823807))),
                ('updated_at', models.DateTimeField(null=True)),
                ('status', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoppingcart', to='ecommerce.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 6, 5, 14, 29, 47, 823807))),
                ('updated_at', models.DateTimeField(null=True)),
                ('product_name', models.CharField(max_length=255)),
                ('product_description', models.TextField(max_length=200)),
                ('product_price', models.IntegerField(default=0)),
                ('product_weight', models.IntegerField(default=0)),
                ('product_brand', models.CharField(max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='ecommerce.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 6, 5, 14, 29, 47, 823807))),
                ('updated_at', models.DateTimeField(null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitem', to='ecommerce.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitem', to='ecommerce.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='ecommerce.user'),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 6, 5, 14, 29, 47, 823807))),
                ('updated_at', models.DateTimeField(null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartitem', to='ecommerce.product')),
                ('shopping_cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartitem', to='ecommerce.shoppingcart')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
