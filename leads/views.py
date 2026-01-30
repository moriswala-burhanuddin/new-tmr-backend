from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import ContactInquiry, WholesaleInquiry
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
