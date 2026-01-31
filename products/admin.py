from django.contrib import admin
from .models import Brand, Category, Product

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (None, {'fields': ('name', 'slug', 'logo', 'description')}),
        ('CMS / Page Content', {
            'fields': ('hero_title', 'hero_subtitle', 'hero_image', 'content', 'html_content')
        }),
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_brands', 'category', 'is_featured')
    list_filter = ('brands', 'category', 'is_featured')
    search_fields = ('name', 'specifications')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_featured',)
    filter_horizontal = ('brands',)

    def get_brands(self, obj):
        return ", ".join([b.name for b in obj.brands.all()])
    get_brands.short_description = 'Brands'
