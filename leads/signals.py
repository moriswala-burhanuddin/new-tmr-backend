from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactInquiry, WholesaleInquiry

@receiver(post_save, sender=ContactInquiry)
def send_contact_notification(sender, instance, created, **kwargs):
    if created:
        subject = f"New Contact Inquiry: {instance.name}"
        message = f"""
        New contact inquiry received.
        
        Name: {instance.name}
        Email: {instance.email}
        Phone: {instance.phone}
        Budget: {instance.budget}
        
        Message:
        {instance.requirement}
        """
        try:
            # Send to admin emails (configured in settings or hardcoded for now)
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL], # Sending to self for now
                fail_silently=True,
            )
        except Exception as e:
            print(f"Failed to send email: {e}")

@receiver(post_save, sender=WholesaleInquiry)
def send_wholesale_notification(sender, instance, created, **kwargs):
    if created:
        subject = f"New Wholesale Inquiry: {instance.business_name}"
        message = f"""
        New wholesale inquiry received.
        
        Business: {instance.business_name}
        Contact: {instance.name}
        Email: {instance.email}
        Phone: {instance.contact_number}
        Brand Interest: {", ".join([b.name for b in instance.brands_interested.all()])}
        Product Interest: {", ".join([p.name for p in instance.products_interested.all()])}
        
        Details:
        {instance.details}
        """
        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=True,
            )
        except Exception as e:
            print(f"Failed to send email: {e}")
