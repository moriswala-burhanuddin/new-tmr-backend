
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from products.models import Product, Brand, Category
from django.utils.text import slugify

# DATA
CATEGORY_NAME = "Hand Tools"
BRAND_NAMES = ["Force", "Kingtony", "Stanley", "TOTAL", "Master Tools", "Inc-Co", "Wiseup"]

PRODUCTS_DATA = [
    ("Snap-Off Blade Knife", "Snap-Off Blade Knife | Hand Tools", "snap off knife, blade knife, hand tools"),
    ("Screwdrivers Set", "Screwdrivers Set | Hand Tools", "screwdrivers set, hand tools, tool set"),
    ("Screw Extractor Set", "Screw Extractor Set | Hand Tools", "screw extractor, broken screw remover, hand tools"),
    ("Rubber Mallet", "Rubber Mallet | Hand Tools", "rubber mallet, soft hammer, hand tools"),
    ("Two Way Mallet", "Two Way Mallet | Hand Tools", "two way mallet, dual head mallet, hand tools"),
    ("Dead Blow Mallet", "Dead Blow Mallet | Hand Tools", "dead blow mallet, soft hammer, hand tools"),
    ("Machinist Hammer", "Machinist Hammer | Hand Tools", "machinist hammer, engineer hammer, hand tools"),
    ("Claw Hammer", "Claw Hammer | Hand Tools", "claw hammer, hammer tool, hand tools"),
    ("Punch Set", "Punch Set | Hand Tools", "punch set, metal punch, hand tools"),
    ("Figure Punch", "Figure Punch | Hand Tools", "figure punch, marking punch, hand tools"),
    ("Cold Chisel Plus", "Cold Chisel Plus | Hand Tools", "cold chisel, masonry chisel, hand tools"),
    ("Cold Chisel Minus", "Cold Chisel Minus | Hand Tools", "cold chisel, metal chisel, hand tools"),
    ("Pump Plier", "Pump Plier | Hand Tools", "pump plier, adjustable plier, hand tools"),
    ("Combination Plier", "Combination Plier | Hand Tools", "combination plier, hand tools, pliers"),
    ("Long Nose Plier", "Long Nose Plier | Hand Tools", "long nose plier, pliers tool, hand tools"),
    ("Jaw Plier", "Jaw Plier | Hand Tools", "jaw plier, locking plier, hand tools"),
    ("Internal Circlip Plier", "Internal Circlip Plier | Hand Tools", "circlip plier, internal plier, hand tools"),
    ("External Circlip Plier", "External Circlip Plier | Hand Tools", "circlip plier, external plier, hand tools"),
    ("Circlip Plier Set", "Circlip Plier Set | Hand Tools", "circlip set, plier set, hand tools"),
    ("Insulated Long Nose Plier", "Insulated Long Nose Plier | Hand Tools", "insulated plier, long nose plier, hand tools"),
    ("Insulated Diagonal Plier", "Insulated Diagonal Plier | Hand Tools", "diagonal plier, insulated cutter, hand tools"),
    ("Insulated Combination Plier", "Insulated Combination Plier | Hand Tools", "insulated plier, combination plier, hand tools"),
    ("Insulated Cable Cutter", "Insulated Cable Cutter | Hand Tools", "cable cutter, insulated cutter, hand tools"),
    ("Hand Riveter", "Hand Riveter | Hand Tools", "hand riveter, rivet gun, hand tools"),
    ("Folding Hand Riveter", "Folding Hand Riveter | Hand Tools", "folding riveter, rivet tool, hand tools"),
    ("G-Clamp", "G-Clamp | Hand Tools", "g clamp, clamping tool, hand tools"),
    ("Chain Clamp Locking Plier", "Chain Clamp Locking Plier | Hand Tools", "chain clamp, locking plier, hand tools"),
    ("Carpenter Pencil", "Carpenter Pencil | Hand Tools", "carpenter pencil, marking tool, hand tools"),
    ("Bolt Cutter", "Bolt Cutter | Hand Tools", "bolt cutter, cutting tool, hand tools"),
    ("Blade Set", "Blade Set | Hand Tools", "blade set, cutting blades, hand tools"),
    ("Bi-Metal Hacksaw Blade Set", "Bi-Metal Hacksaw Blade Set | Hand Tools", "hacksaw blade, bi metal blade, hand tools"),
    ("Aluminum Rivet", "Aluminum Rivet | Hand Tools", "aluminum rivet, fastening tool, hand tools"),
    ("Adjustable Wrench", "Adjustable Wrench | Hand Tools", "adjustable wrench, spanner, hand tools"),
    ("Combination Spanner Set", "Combination Spanner Set | Hand Tools", "spanner set, combination spanner, hand tools"),
    ("Electrical Tool Set", "Electrical Tool Set | Hand Tools", "electrical tools, tool set, hand tools"),
    ("Drive Impact Socket", "Drive Impact Socket | Hand Tools", "impact socket, drive socket, hand tools"),
    ("3/4 Drive Socket Set", "3/4 NOT_QUOTE Drive Socket Set | Hand Tools", "socket set, drive socket, hand tools"),
    ("1/2 NOT_QUOTE Drive Socket Set", "1/2 NOT_QUOTE Drive Socket Set | Hand Tools", "socket set, drive socket, hand tools"),
    ("1/2 NOT_QUOTE Drive Ratchet Handle", "1/2 NOT_QUOTE Drive Ratchet Handle | Hand Tools", "ratchet handle, socket tool, hand tools"),
    ("1/2 NOT_QUOTE Drive L-Handle", "1/2 NOT_QUOTE Drive L Handle | Hand Tools", "l handle, socket tool, hand tools"),
    ("Long Arm Hex Key Set", "Long Arm Hex Key Set | Hand Tools", "hex key set, allen key, hand tools"),
    ("Precision Screwdrivers Set", "Precision Screwdrivers Set | Hand Tools", "precision screwdriver, small tools, hand tools"),
    ("Mini Pick & Hook Set", "Mini Pick and Hook Set | Hand Tools", "pick hook set, precision tools, hand tools"),
    ("Pipe Threading Set", "Pipe Threading Set | Hand Tools", "pipe threading, threading tool, hand tools"),
    ("Torque Wrench", "Torque Wrench | Hand Tools", "torque wrench, precision wrench, hand tools"),
    ("Voltage Tester", "Voltage Tester | Hand Tools", "voltage tester, electrical tester, hand tools"),
    ("Spirit Level", "Spirit Level | Hand Tools", "spirit level, leveling tool, hand tools"),
]

def run():
    print("Starting product import...")
    
    # 1. Get or Create Category
    # Robust way: check by slug first to avoid IntegrityError if name case differs
    cat_slug = slugify(CATEGORY_NAME)
    try:
        category = Category.objects.get(slug=cat_slug)
        print(f"Found Category (by slug): {category.name}")
    except Category.DoesNotExist:
        category, created = Category.objects.get_or_create(name=CATEGORY_NAME)
        if created:
            print(f"Created Category: {CATEGORY_NAME}")
        else:
            print(f"Found Category: {CATEGORY_NAME}")

    # 2. Get or Create Brands
    brands = []
    for brand_name in BRAND_NAMES:
        brand_slug = slugify(brand_name)
        try:
            brand = Brand.objects.get(slug=brand_slug)
            brands.append(brand)
            # print(f"Found Brand: {brand.name}") # verbose
        except Brand.DoesNotExist:
            brand, created = Brand.objects.get_or_create(name=brand_name)
            brands.append(brand)
            if created:
                print(f"Created Brand: {brand_name}")
    
    # 3. Create Products
    for name, title, keywords in PRODUCTS_DATA:
        # Sanitize quotes
        final_name = name.replace("NOT_QUOTE", "\"")
        final_title = title.replace("NOT_QUOTE", "\"")
        product_slug = slugify(final_name)
        
        # Check by slug to ensure we don't duplicate or crash
        if Product.objects.filter(slug=product_slug).exists():
            print(f"Skipping {final_name} - Already exists (by slug)")
            continue
            
        try:
            product = Product.objects.create(
                name=final_name,
                category=category,
                is_featured=True,
                meta_title=final_title,
                meta_keywords=keywords,
                specifications="High quality industrial hand tool."
            )
            product.brands.set(brands)
            product.save()
            print(f"Created Product: {final_name}")
        except Exception as e:
            print(f"Error creating {final_name}: {e}")

if __name__ == "__main__":
    run()
