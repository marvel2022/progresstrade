# Generated by Django 4.0.5 on 2022-06-14 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0002_alter_product_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64, verbose_name='Имя')),
                ('image', models.ImageField(upload_to='customers-images', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Покупатель',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64, verbose_name='Имя')),
                ('image', models.ImageField(upload_to='seller-images', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(blank=True, choices=[('NEW', 'New'), ('POP', 'Popular')], max_length=64, null=True, verbose_name='Тип'),
        ),
    ]