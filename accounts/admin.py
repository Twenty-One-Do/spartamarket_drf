from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User

@admin.register(User)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'username', "date_joined")
    search_fields = ("nickname", "username")
    list_filter = ("date_joined",)
    date_hierarchy = "date_joined"
    ordering = ("-date_joined",)