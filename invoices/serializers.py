from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    line_total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    class Meta:
        model = InvoiceDetail
        fields = ['id', 'description', 'quantity', 'price', 'line_total']

class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True)
    class Meta:
        model = Invoice
        fields = ['id', 'invoice_number', 'date', 'customer_name', 'details']

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        invoice = Invoice.objects.create(**validated_data)
        for detail_data in details_data:
            InvoiceDetail.objects.create(invoice=invoice, **detail_data)
        return invoice

    def update(self, instance, validated_data):
        details_data = validated_data.pop('details', [])
        instance.invoice_number = validated_data.get('invoice_number', instance.invoice_number)
        instance.date = validated_data.get('date', instance.date)
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.save()
        for detail_data in details_data:
            detail_id = detail_data.get('id', None)
            if detail_id:
                detail_instance = InvoiceDetail.objects.get(id=detail_id, invoice=instance)
                detail_instance.description = detail_data.get('description', detail_instance.description)
                detail_instance.quantity = detail_data.get('quantity', detail_instance.quantity)
                detail_instance.price = detail_data.get('price', detail_instance.price)
                detail_instance.save()
            else:
                InvoiceDetail.objects.create(invoice=instance, **detail_data)

        return instance
