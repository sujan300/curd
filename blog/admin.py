from django.contrib import admin
from blog.models import Post
# Register your models here.



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display        = ("id","title","content")
    list_display_links  = ("title","content")