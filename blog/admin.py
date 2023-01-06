from django.contrib import admin
from .models import BlogPost, BlogComment

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date')
    search_fields = ('title',)
    list_per_page = 20

@admin.action(description='Show Comment')
def showComment(modelAdmin, request, queryset):
    queryset.update(show_comment=True)

@admin.action(description='Hide Comment')
def hideComment(modelAdmin, request, queryset):
    queryset.update(show_comment=False)

class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'blog', 'comment_date', 'show_comment')
    search_fields = ('name',)
    actions = [showComment, hideComment]
    list_per_page = 20


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
