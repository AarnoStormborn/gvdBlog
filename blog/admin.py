from django.contrib import admin
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date')
    search_fields = ('title',)
    list_per_page = 20


admin.site.register(BlogPost, BlogPostAdmin)
