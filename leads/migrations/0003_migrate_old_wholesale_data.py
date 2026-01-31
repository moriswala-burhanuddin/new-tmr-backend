from django.db import migrations

def migrate_data(apps, schema_editor):
    WholesaleInquiry = apps.get_model('leads', 'WholesaleInquiry')
    for inquiry in WholesaleInquiry.objects.all():
        if inquiry.product_interested_old:
            inquiry.products_interested.add(inquiry.product_interested_old)
        if inquiry.brand_interested_old:
            inquiry.brands_interested.add(inquiry.brand_interested_old)

def reverse_migrate_data(apps, schema_editor):
    WholesaleInquiry = apps.get_model('leads', 'WholesaleInquiry')
    for inquiry in WholesaleInquiry.objects.all():
        inquiry.product_interested_old = inquiry.products_interested.first()
        inquiry.brand_interested_old = inquiry.brands_interested.first()
        inquiry.save()

class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_remove_wholesaleinquiry_brand_interested_and_more'),
    ]

    operations = [
        migrations.RunPython(migrate_data, reverse_migrate_data),
    ]
