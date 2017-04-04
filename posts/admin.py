from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Post


admin.site.unregister(User)
admin.site.unregister(Group)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
