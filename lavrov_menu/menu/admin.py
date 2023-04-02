from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from menu.models import MenuItem


class MenuItemMPTTModelAdmin(DjangoMpttAdmin):
    mptt_level_indent = 20
    prepopulated_fields = {"url": ("name",)}

admin.site.register(MenuItem, MenuItemMPTTModelAdmin)



