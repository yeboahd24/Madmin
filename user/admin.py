from django.contrib import admin
from .models import MadminCategory, CategoryIndexTitle, Comments


@admin.register(MadminCategory)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',), }


admin.site.register(CategoryIndexTitle)
admin.site.register(Comments)
