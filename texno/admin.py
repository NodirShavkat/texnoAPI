from django.contrib import admin
from .models import Category, Product, Image

admin.site.register(Product)
admin.site.register(Image)

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["id", 'name', 'slug']
    prepopulated_fields = {'slug':('name',)}
