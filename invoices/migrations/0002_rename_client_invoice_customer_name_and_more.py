# Generated by Django 5.1.3 on 2024-11-13 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='client',
            new_name='customer_name',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='number',
            new_name='invoice_number',
        ),
        migrations.RenameField(
            model_name='invoicedetail',
            old_name='unit_price',
            new_name='price',
        ),
    ]