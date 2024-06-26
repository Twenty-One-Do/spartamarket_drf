# Generated by Django 5.0.4 on 2024-04-30 03:44

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
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='no tag', max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=100)),
                ('content', models.TextField()),
                ('likes_num', models.PositiveIntegerField(default=0)),
                ('views_num', models.PositiveIntegerField(default=0)),
                ('category', models.CharField(choices=[('', '')], max_length=10)),
                ('image', models.ImageField(upload_to='../static/images/')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Likes_Relation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_products', to=settings.AUTH_USER_MODEL)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_users', to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Tag_Relation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='products.product')),
                ('tag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Views_Relation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='views_users', to='products.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='views_products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
