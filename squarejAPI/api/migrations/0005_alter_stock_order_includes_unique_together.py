# Generated by Django 4.0 on 2021-12-17 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_ord_includes_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='stock_order_includes',
            unique_together={('order_id', 'upc')},
        ),
    ]
