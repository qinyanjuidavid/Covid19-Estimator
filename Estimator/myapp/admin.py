from django.contrib import admin
from myapp.models import Covid19,Impact,SevereImpact

admin.site.register(Impact)
admin.site.register(SevereImpact)
admin.site.register(Covid19)
