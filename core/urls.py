from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from products.views import BrandViewSet, CategoryViewSet, ProductViewSet, HomeCategoryViewSet
from leads.views import ContactInquiryViewSet, WholesaleInquiryViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'home-categories', HomeCategoryViewSet)

from pages.views import serve_react_app
from django.urls import path, include, re_path

from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/login/', views.obtain_auth_token),
    path('api/', include(router.urls)),
    path('api/leads/', include('leads.urls')),
    path('api/pages/', include('pages.urls')),
    
    # React App Entry Point (Server-Side Injection)
    path('', serve_react_app, name='index'),
    # Catch-all for React Router (excluding api/admin/media/static)
    re_path(r'^(?!api|admin|media|static).*$', serve_react_app, name='react-app'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
