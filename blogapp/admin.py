from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display=["id","title","blog_image","description"]
    search_fields=["title","description"]
    list_filter=["title"]

admin.site.register(Blog,BlogAdmin)