from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "product_type",
        "category",
        "slug",
        "description",
        "regular_price",
        "is_active",
        "created_at",
        "updated_at",
    ]
    list_filter = ["title", "is_active"]
    list_editable = ["regular_price", "is_active"]
    prepopulated_fields = {"slug": ("title",)}
