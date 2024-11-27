from django.contrib import admin

from sales.models import Category,Product,Category1,Comment, CategoryAttribute

admin.site.register(Category1)
admin.site.register(Comment)
admin.site.register(CategoryAttribute)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {'slug': ('name',)}    