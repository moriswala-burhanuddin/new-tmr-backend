from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactInquiryViewSet, WholesaleInquiryViewSet, DashboardStatsView

router = DefaultRouter()
router.register(r'contact', ContactInquiryViewSet)
router.register(r'wholesale', WholesaleInquiryViewSet)

urlpatterns = [
    path('stats/', DashboardStatsView.as_view(), name='dashboard-stats'),
    path('', include(router.urls)),
]
