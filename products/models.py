from django.db import models
from django.utils.text import slugify

class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)
    logo = models.ImageField(upload_to='brands/', blank=True, null=True)
    description = models.TextField(blank=True)

    # CMS / Page Content
    hero_title = models.CharField(max_length=200, blank=True)
    hero_subtitle = models.TextField(blank=True)
    hero_image = models.ImageField(upload_to='brands/hero/', blank=True)
    
    content = models.TextField(blank=True, help_text="Main content (HTML/Text)")
    html_content = models.TextField(blank=True, help_text="Additional Detail Text (HTML/Text)")
    
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    brands = models.ManyToManyField(Brand, related_name='products', blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True, blank=True)
    
    # Specifications
    specifications = models.TextField(help_text="Detailed text specifications", blank=True)
    
    # Images
    image = models.ImageField(upload_to='products/', help_text="Main product image")
    
    # Promotion / Feature
    is_featured = models.BooleanField(default=False, help_text="Show on Home Page")
    
    # SEO Fields
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True, help_text="Meta keywords for search engines")
    og_image = models.ImageField(upload_to='products/og/', blank=True, help_text="Social Media Share Image")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
