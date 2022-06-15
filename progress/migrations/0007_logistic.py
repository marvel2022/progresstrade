# Generated by Django 4.0.5 on 2022-06-15 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0006_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('place_name', models.CharField(max_length=100, verbose_name='Куда')),
                ('price', models.CharField(max_length=64, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Логистика',
                'verbose_name_plural': 'Логистика',
            },
        ),
    ]
