from django.contrib import admin
from .models import *


@admin.register(CustomUserModel)
class CustomUserModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ('text',)
    autocomplete_fields = ('comment_reply',)
