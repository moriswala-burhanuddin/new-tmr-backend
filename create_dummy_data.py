
import os
import django
import random
from decimal import Decimal

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from products.models import Brand, Category, Product
from pages.models import HomePage, AboutPage

def create_data():
    print("Creating dummy data...")
    
    # Create Brands
    brands_data = [
        {"name": "Nike", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Logo_NIKE.svg/1200px-Logo_NIKE.svg.png"},
        {"name": "Adidas", "logo": "https://upload.wikimedia.org/wikipedia/commons/2/20/Adidas_Logo.svg"},
        {"name": "Puma", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Puma_Logo.png/800px-Puma_Logo.png"},
        {"name": "Reebok", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Reebok_Red_Delta_Logo.svg/2560px-Reebok_Red_Delta_Logo.svg.png"},
        {"name": "Under Armour", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Under_Armour_Logo_2023.svg/1200px-Under_Armour_Logo_2023.svg.png"}
    ]
    brands = []
    for b_data in brands_data:
        brand, created = Brand.objects.get_or_create(name=b_data["name"], defaults={'logo': b_data["logo"]})
        if not created and not brand.logo:
            brand.logo = b_data["logo"]
            brand.save()
        brands.append(brand)
        print(f"Brand: {b_data['name']} {'(Created)' if created else '(Exists)'}")

    # Create Categories
    categories_data = ["Shoes", "Apparel", "Accessories", "Sports Gear"]
    categories = []
    for c_name in categories_data:
        category, created = Category.objects.get_or_create(name=c_name, defaults={'slug': c_name.lower().replace(" ", "-")})
        categories.append(category)
        print(f"Category: {c_name} {'(Created)' if created else '(Exists)'}")

    # Create Products
    # Using simple unsplash placeholder images
    product_images = [
        "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=800",
        "https://images.unsplash.com/photo-1549298916-b41d501d3772?w=800",
        "https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?w=800",
        "https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=800",
        "https://images.unsplash.com/photo-1539185441755-769473a23570?w=800"
    ]

    for i in range(10):
        brand = random.choice(brands)
        category = random.choice(categories)
        name = f"{brand.name} {category.name} Item {i+1}"
        slug = name.lower().replace(" ", "-")
        product, created = Product.objects.get_or_create(
            name=name,
            defaults={
                'slug': slug,
                'brand': brand,
                'category': category,
                'price': Decimal(random.randint(50, 200)),
                'specifications': "High quality material. Perfect for daily use.",
                'is_featured': i % 2 == 0,
                'image': random.choice(product_images)
            }
        )
        if not created and not product.image:
             product.image = random.choice(product_images)
             product.save()
             
        print(f"Product: {name} {'(Created)' if created else '(Exists)'}")

    # Create Home Page Config
    home, created = HomePage.objects.get_or_create(
        defaults={
            'hero_title': "Elevate Your Style with TMR",
            'facebook_url': "https://facebook.com",
            'instagram_url': "https://instagram.com",
        }
    )
    if not created:
        home.hero_title = "Elevate Your Style with TMR"
        home.save()
        
    print(f"Home Page Config: {'Created' if created else 'Exists'}")

    # Create About Page Config
    about, created = AboutPage.objects.get_or_create(
        defaults={
            'title': "About TMR Project",
            'content': "We are a leading provider of specific products."
        }
    )
    print(f"About Page Config: {'Created' if created else 'Exists'}")

if __name__ == "__main__":
    create_data()
