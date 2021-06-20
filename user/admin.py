from django.contrib import admin
from .models import Category, CategoryIndexTitle


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',), }


admin.site.register(CategoryIndexTitle)