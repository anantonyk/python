from django.contrib import admin
from .models import Post

admin.site.register(Post)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['author', 'created_date']

