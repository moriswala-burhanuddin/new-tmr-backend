from rest_framework import serializers
from .models import ContactInquiry, WholesaleInquiry
from products.serializers import BrandSerializer, ProductSerializer

class ContactInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInquiry
        fields = '__all__'

class WholesaleInquirySerializer(serializers.ModelSerializer):
    product_details = ProductSerializer(source='product_interested', read_only=True)
    brand_details = BrandSerializer(source='brand_interested', read_only=True)

    class Meta:
        model = WholesaleInquiry
        fields = '__all__'
