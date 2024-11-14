# Generated by Django 5.1.3 on 2024-11-13 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_rename_client_invoice_customer_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='customer_name',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='invoice_number',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='invoicedetail',
            old_name='price',
            new_name='unit_price',
        ),
    ]
