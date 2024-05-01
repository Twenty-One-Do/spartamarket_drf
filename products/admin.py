from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, ProductCategory

@admin.register(Product)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'writer',
                    "category",
                    "likes_num",
                    "views_num",
                    "last_updated",
                    "date_created")
    search_fields = ("title", "writer")
    list_filter = ("date_created", "category")
    date_hierarchy = "date_created"
    ordering = (
        "-date_created",
        "-likes_num",
        "-views_num",
    )

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'description',)
    search_fields = ("name", "description")
    list_filter = ("name", )
    ordering = ("-id", "-name",)