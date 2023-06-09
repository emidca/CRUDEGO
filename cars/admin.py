from django.contrib import admin
from .models import Car, Description


class DescriptionInline(admin.TabularInline):
    model = Description


class CarAdmin(admin.ModelAdmin):
    inlines = [DescriptionInline]


admin.site.register(Car, CarAdmin)
admin.site.register(Description)
