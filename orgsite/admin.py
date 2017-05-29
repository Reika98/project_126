from django.contrib import admin
from .models import Organization, Activity, FAQs

admin.site.register(Organization)
admin.site.register(Activity)
admin.site.register(FAQs)