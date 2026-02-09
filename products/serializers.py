from rest_framework import serializers
from .models import Brand, Category, Product, HomeCategory

class HomeCategorySerializer(serializers.ModelSerializer):
    category_slug = serializers.CharField(source='category.slug', read_only=True)
    display_title = serializers.CharField(source='get_title', read_only=True)
    display_image = serializers.CharField(source='get_image', read_only=True)

    class Meta:
        model = HomeCategory
        fields = ['id', 'category', 'category_slug', 'title', 'image', 'order', 'display_title', 'display_image']

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
    categories = CategorySerializer(many=True, read_only=True)
    
    brand_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Brand.objects.all(), source='brands', write_only=True, required=False
    )
    category_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Category.objects.all(), source='categories', write_only=True, required=False
    )
    
    class Meta:
        model = Product
        fields = '__all__'
