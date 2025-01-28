from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Logo
# Register your models here.
admin.site.register(Logo)
admin.site.unregister(Group)
admin.site.site_title = 'ORTOUCHE'
admin.site.site_header = 'Ortouche administration'