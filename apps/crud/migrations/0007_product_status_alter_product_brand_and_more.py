# Generated by Django 4.0.2 on 2022-03-07 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0006_alter_product_brand_alter_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=30, verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=150, verbose_name='Categoria'),
        ),
    ]
