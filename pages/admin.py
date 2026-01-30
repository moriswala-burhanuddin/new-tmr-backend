from django.contrib import admin
from .models import HomePage, AboutPage, ContactPage, WholesalePage, BrandPageContent

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    fieldsets = (
        ('SEO', {'fields': ('seo_title', 'seo_description')}),
        ('Hero', {'fields': ('hero_title', 'hero_subtitle', 'hero_image', 'hero_image_1', 'hero_image_2', 'hero_image_3', 'hero_image_4', 'hero_image_5')}),
        ('Social Links', {'fields': ('facebook_url', 'instagram_url', 'tiktok_url', 'linkedin_url', 'youtube_url')}),
        ('Content', {'fields': ('about_section_title', 'about_section_content', 'content')}),
    )

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    fields = ('seo_title', 'seo_description', 'hero_title', 'hero_subtitle', 'hero_image', 'content')

@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    fields = ('seo_title', 'seo_description', 'hero_title', 'hero_subtitle', 'hero_image', 'content', 'address', 'phone', 'email', 'map_embed_url')

@admin.register(WholesalePage)
class WholesalePageAdmin(admin.ModelAdmin):
    fields = ('seo_title', 'seo_description', 'hero_title', 'hero_subtitle', 'hero_image', 'content')
    
@admin.register(BrandPageContent)
class BrandPageContentAdmin(admin.ModelAdmin):
    fields = ('seo_title', 'seo_description', 'hero_title', 'hero_subtitle', 'hero_image', 'content')
