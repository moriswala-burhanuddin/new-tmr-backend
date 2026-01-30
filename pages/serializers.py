from rest_framework import serializers
from .models import HomePage, AboutPage, ContactPage, WholesalePage, BrandPageContent

class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = '__all__'

class AboutPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutPage
        fields = '__all__'

class ContactPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPage
        fields = '__all__'

class WholesalePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WholesalePage
        fields = '__all__'

class BrandPageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandPageContent
        fields = '__all__'
