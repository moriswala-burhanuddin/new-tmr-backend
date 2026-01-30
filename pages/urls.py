from django.urls import path
from .views import (
    HomePageView, AboutPageView, ContactPageView, 
    WholesalePageView, BrandPageContentView
)

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home-page'),
    path('about/', AboutPageView.as_view(), name='about-page'),
    path('contact/', ContactPageView.as_view(), name='contact-page'),
    path('wholesale/', WholesalePageView.as_view(), name='wholesale-page'),
    path('brand/', BrandPageContentView.as_view(), name='brand-page-content'),
]
