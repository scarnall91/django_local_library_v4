from django.contrib import admin
from .models import Resort,Choice

@admin.register(Resort)
class ResortAdmin(admin.ModelAdmin):
    list_display = ('resort_name','beginner','intermediate','expert')

admin.site.register(Choice)
