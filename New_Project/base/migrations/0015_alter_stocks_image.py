# Generated by Django 4.0.1 on 2022-02-03 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_stocks_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='image',
            field=models.ImageField(upload_to='img/base/products'),
        ),
    ]
