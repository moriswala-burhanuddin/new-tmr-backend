from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactInquiryViewSet, WholesaleInquiryViewSet

router = DefaultRouter()
router.register(r'contact', ContactInquiryViewSet)
router.register(r'wholesale', WholesaleInquiryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
