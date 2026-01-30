from django.db import models

class ContactInquiry(models.Model):
    name = models.CharField(max_length=100)
    business_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    website = models.URLField(blank=True)
    budget = models.CharField(max_length=100, blank=True)
    requirement = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Inquiry from {self.name}"

class WholesaleInquiry(models.Model):
    name = models.CharField(max_length=100)
    business_name = models.CharField(max_length=150)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    
    # Interests
    product_interested = models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True, blank=True)
    brand_interested = models.ForeignKey('products.Brand', on_delete=models.SET_NULL, null=True, blank=True)
    
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Wholesale: {self.business_name}"
