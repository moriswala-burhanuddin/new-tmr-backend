from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer

class BaseProductViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]

class BrandViewSet(BaseProductViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class CategoryViewSet(BaseProductViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(BaseProductViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        is_featured = self.request.query_params.get('featured')
        category_slug = self.request.query_params.get('category')
        brand_id = self.request.query_params.get('brand')
        
        if is_featured:
            queryset = queryset.filter(is_featured=True)
            
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
            
        if brand_id:
            queryset = queryset.filter(brand__id=brand_id)
            
        return queryset
