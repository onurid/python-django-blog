from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['Title', 'PublishDate']
    list_filter = ['PublishDate']
    search_fields = ['Title']

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
