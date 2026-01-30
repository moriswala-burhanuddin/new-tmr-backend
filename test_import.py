import os
import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()
print("Setup complete")
from django.contrib import admin
print("Admin imported")
