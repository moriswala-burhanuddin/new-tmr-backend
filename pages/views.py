from rest_framework import views, response, status, permissions
from .models import HomePage, AboutPage, ContactPage, WholesalePage, BrandPageContent
from .serializers import (
    HomePageSerializer, AboutPageSerializer, ContactPageSerializer, 
    WholesalePageSerializer, BrandPageContentSerializer
)

class PageView(views.APIView):
    model = None
    serializer_class = None
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Allow public read, admin write (if authenticated)

    def get(self, request):
        page = self.model.objects.first()
        if not page:
             return response.Response({}) 
        serializer = self.serializer_class(page)
        return response.Response(serializer.data)

    def patch(self, request):
        if not request.user.is_staff:
            return response.Response({'detail': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)

        page = self.model.objects.first()
        if not page:
            # If page doesn't exist yet, we create it.
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return response.Response(serializer.data, status=status.HTTP_201_CREATED)
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Update existing
        serializer = self.serializer_class(page, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HomePageView(PageView):
    model = HomePage
    serializer_class = HomePageSerializer

class AboutPageView(PageView):
    model = AboutPage
    serializer_class = AboutPageSerializer

class ContactPageView(PageView):
    model = ContactPage
    serializer_class = ContactPageSerializer

class WholesalePageView(PageView):
    model = WholesalePage
    serializer_class = WholesalePageSerializer
    
from django.conf import settings
from django.http import HttpResponse
import os

def serve_react_app(request):
    """
    Serves the compiled React app with injected SEO tags.
    """
    try:
        path = os.path.join(settings.FRONTEND_DIR, 'dist', 'index.html')
        with open(path, 'r', encoding='utf-8') as file:
            html_content = file.read()
            
        # SEO Injection
        seo_title = "TMR Project"
        seo_desc = "Industrial Hardware"

        path_stripped = request.path.strip('/')
        
        page_obj = None
        if path_stripped == '' or path_stripped == 'home':
            page_obj = HomePage.objects.first()
        elif path_stripped == 'about':
            page_obj = AboutPage.objects.first()
        elif path_stripped == 'contact':
            page_obj = ContactPage.objects.first()
        elif path_stripped == 'wholesale':
            page_obj = WholesalePage.objects.first()
            
        if page_obj:
            seo_title = getattr(page_obj, 'seo_title', seo_title) or seo_title
            seo_desc = getattr(page_obj, 'seo_description', seo_desc) or seo_desc
            
        # Replace Title
        # Note: We look for the exact string we know is in the index.html
        html_content = html_content.replace('<title>TMR Project</title>', f'<title>{seo_title}</title>')
        
        # Inject Description
        # We insert it before the closing head tag
        meta_tag = f'<meta name="description" content="{seo_desc}" />'
        html_content = html_content.replace('</head>', f'{meta_tag}</head>')
            
        return HttpResponse(html_content)
    except FileNotFoundError:
        return HttpResponse(
            "Frontend build not found. Please run 'npm run build' in the frontend directory.", 
            status=501
        )

class BrandPageContentView(PageView):
    model = BrandPageContent
    serializer_class = BrandPageContentSerializer
