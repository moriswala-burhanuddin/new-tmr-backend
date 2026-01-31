from django.db import models
from django.core.exceptions import ValidationError

class Page(models.Model):
    title = models.CharField(max_length=200, help_text="Internal title", default="Default Title")
    slug = models.SlugField(unique=True, help_text="URL slug", default="default-slug")
    
    # SEO Fields
    seo_title = models.CharField(max_length=200, blank=True, help_text="Browser tab title")
    seo_description = models.TextField(blank=True, help_text="Meta description for search engines")
    seo_keywords = models.TextField(blank=True, help_text="Meta keywords for search engines")
    
    # Content
    hero_title = models.CharField(max_length=200, blank=True)
    hero_subtitle = models.TextField(blank=True)
    hero_image = models.ImageField(upload_to='pages/hero/', blank=True)
    
    content = models.TextField(blank=True, help_text="Main content (HTML/Text)")
    html_content = models.TextField(blank=True, help_text="Additional Detail Text (HTML/Text)")
    
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class HomePage(Page):
    # Singleton pattern enforcement
    def save(self, *args, **kwargs):
        if not self.pk and HomePage.objects.exists():
            raise ValidationError('There can be only one Home Page instance')
        return super(HomePage, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Home Page Content"
        verbose_name_plural = "Home Page Content"

    # Social Media Links
    facebook_url = models.URLField(blank=True, verbose_name="Facebook URL")
    instagram_url = models.URLField(blank=True, verbose_name="Instagram URL")
    tiktok_url = models.URLField(blank=True, verbose_name="TikTok URL")
    linkedin_url = models.URLField(blank=True, verbose_name="LinkedIn URL")
    youtube_url = models.URLField(blank=True, verbose_name="YouTube URL")
    
    # Home Specific Sections
    about_section_title = models.CharField(max_length=200, default="About Us")
    about_section_content = models.TextField(blank=True)

    # Hero Slider Images
    hero_image_1 = models.ImageField(upload_to='home/hero/', blank=True)
    hero_image_2 = models.ImageField(upload_to='home/hero/', blank=True)
    hero_image_3 = models.ImageField(upload_to='home/hero/', blank=True)
    hero_image_4 = models.ImageField(upload_to='home/hero/', blank=True)
    hero_image_5 = models.ImageField(upload_to='home/hero/', blank=True)

    # Stats / Social Proof
    clients_served_count = models.CharField(max_length=50, default="100+")
    expert_support_text = models.CharField(max_length=100, default="24/7 EXPERT SUPPORT")
    
class AboutPage(Page):
    class Meta:
        verbose_name = "About Page Content"
        verbose_name_plural = "About Page Content"

    # Stats
    clients_served_count = models.CharField(max_length=50, default="100+")
    expert_support_text = models.CharField(max_length=100, default="24/7 EXPERT SUPPORT")

class ContactPage(Page):
    class Meta:
        verbose_name = "Contact Page Content"
        verbose_name_plural = "Contact Page Content"
    
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    map_embed_url = models.TextField(blank=True, help_text="Google Maps Embed URL")

class WholesalePage(Page):
    class Meta:
        verbose_name = "Wholesale Page Content"
        verbose_name_plural = "Wholesale Page Content"

class BrandPageContent(Page):
    class Meta:
        verbose_name = "Brand Page Content (Generic)"
        verbose_name_plural = "Brand Page Content (Generic)"
