# Generated by Django 3.0.8 on 2020-07-22 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='qantity',
            new_name='quantity',
        ),
    ]
