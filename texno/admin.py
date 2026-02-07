from django.contrib import admin
from .models import Category, Product, Image, Comment, Order

admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Comment)

@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ["id", 'user', 'product']

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["id", 'name', 'slug']
    prepopulated_fields = {'slug':('name',)}
