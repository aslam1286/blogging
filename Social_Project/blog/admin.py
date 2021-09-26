
from django.contrib import admin

from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','content','date_posted','author']

admin.site.register(Post,PostAdmin)