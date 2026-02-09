from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Brand, Category, Product, HomeCategory
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer, HomeCategorySerializer

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
            # support comma-separated slugs or multiple slugs in query params
            category_slugs = category_slug.split(',')
            queryset = queryset.filter(categories__slug__in=category_slugs).distinct()
            
        if brand_id:
            queryset = queryset.filter(brands__id=brand_id)
            
        return queryset

class HomeCategoryViewSet(BaseProductViewSet):
    queryset = HomeCategory.objects.all()
    serializer_class = HomeCategorySerializer
