from rest_framework import serializers
from .models import Brand, Category, Product

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        read_only_fields = ('created_at',)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    brands = BrandSerializer(many=True, read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=False, allow_null=True)
    category_details = CategorySerializer(source='category', read_only=True)
    
    brand_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Brand.objects.all(), source='brands', write_only=True, required=False
    )
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True, required=False, allow_null=True
    )
    
    class Meta:
        model = Product
        fields = '__all__'
