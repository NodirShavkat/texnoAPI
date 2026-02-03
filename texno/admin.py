from django.contrib import admin
from .models import Category, Product, Image, Comment

admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Comment)

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["id", 'name', 'slug']
    prepopulated_fields = {'slug':('name',)}
