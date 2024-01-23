from django.contrib import admin
from .models import BlogLists, BlogUserComments,BlogUsersLikes
# Register your models here.

admin.site.register(BlogLists)
admin.site.register(BlogUserComments)
admin.site.register(BlogUsersLikes)
