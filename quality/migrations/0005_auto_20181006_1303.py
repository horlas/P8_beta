# Generated by Django 2.0 on 2018-10-06 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quality', '0004_delete_custonusermodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='substitutproduct',
            old_name='selected_product',
            new_name='selected_product_id',
        ),
    ]
