from django.contrib import admin

from .models import Comment, Post


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_date', 'post', 'parent', 'depth_level')
    readonly_fields = ('depth_level',)


# admin.site.register(CommentToComment)
# admin.site.register(CommentToPost)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post)
