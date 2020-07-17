from django.contrib import admin
from .models import Linkman

# Register your models here.
@admin.register(Linkman)
class LinkmanAdmin(admin.ModelAdmin):
    pass