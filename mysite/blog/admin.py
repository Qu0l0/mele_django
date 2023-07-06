from django.contrib import admin

from blog.models import Post


# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'published', 'status']
    list_filter = ['author', 'status', 'created', 'published']
    search_fields = ['title', 'body', 'author']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'published'
    ordering = ['status', 'published']
