from rest_framework import serializers
from .models import ContactInquiry, WholesaleInquiry
from products.models import Product, Brand
from products.serializers import BrandSerializer, ProductSerializer

class ContactInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInquiry
        fields = '__all__'

class WholesaleInquirySerializer(serializers.ModelSerializer):
    product_details = ProductSerializer(source='products_interested', many=True, read_only=True)
    brand_details = BrandSerializer(source='brands_interested', many=True, read_only=True)
    
    product_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Product.objects.all(), source='products_interested', write_only=True, required=False
    )
    brand_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Brand.objects.all(), source='brands_interested', write_only=True, required=False
    )

    class Meta:
        model = WholesaleInquiry
        fields = '__all__'
