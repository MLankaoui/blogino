from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Category, Post, Comment


admin.site.site_header = "Blogino Admin"
admin.site.site_title = "Blogino Admin Portal"
admin.site.index_title = "Welcome to Blogino Admin Portal"

@admin.register(Category)
class CustomAdminClass(ModelAdmin):
    pass


@admin.register(Post)
class CustomAdminClass(ModelAdmin):
    pass


@admin.register(Comment)
class CustomAdminClass(ModelAdmin):
    pass