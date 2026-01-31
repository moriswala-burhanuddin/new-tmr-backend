from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import ContactInquiry, WholesaleInquiry
from products.models import Product, Brand
from .serializers import ContactInquirySerializer, WholesaleInquirySerializer

class BaseInquiryViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAdminUser()]

class ContactInquiryViewSet(BaseInquiryViewSet):
    """
    Allow creation of Contact Inquiries.
    """
    queryset = ContactInquiry.objects.all()
    serializer_class = ContactInquirySerializer

class WholesaleInquiryViewSet(BaseInquiryViewSet):
    """
    Allow creation of Wholesale Inquiries.
    """
    queryset = WholesaleInquiry.objects.all()
    serializer_class = WholesaleInquirySerializer

class DashboardStatsView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        total_products = Product.objects.count()
        total_brands = Brand.objects.count()
        
        unresolved_contact = ContactInquiry.objects.filter(is_resolved=False).count()
        unresolved_wholesale = WholesaleInquiry.objects.filter(is_resolved=False).count()
        
        # Combined recent activity
        recent_contacts = ContactInquiry.objects.order_by('-created_at')[:10]
        recent_wholesales = WholesaleInquiry.objects.order_by('-created_at')[:10]
        
        activity = []
        for c in recent_contacts:
            activity.append({
                'id': f"C-{c.id}",
                'type': 'General Inquiry',
                'name': c.name,
                'date': c.created_at,
                'is_resolved': c.is_resolved
            })
        for w in recent_wholesales:
            activity.append({
                'id': f"W-{w.id}",
                'type': 'Wholesale Inquiry',
                'name': w.name,
                'date': w.created_at,
                'is_resolved': w.is_resolved
            })
            
        # Sort by date
        activity.sort(key=lambda x: x['date'], reverse=True)
        
        return Response({
            'total_products': total_products,
            'total_brands': total_brands,
            'new_inquiries': unresolved_contact + unresolved_wholesale,
            'system_health': '100%',
            'recent_activity': activity[:10]
        })
