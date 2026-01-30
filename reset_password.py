import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth.models import User

try:
    user = User.objects.get(username='admin')
    user.set_password('password123')
    user.save()
    print("Password for 'admin' reset to 'password123'")
except User.DoesNotExist:
    User.objects.create_superuser('admin', 'admin@example.com', 'password123')
    print("Created new superuser 'admin'")
