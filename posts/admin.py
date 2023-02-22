from django.contrib import admin
from posts.models import  BlogPost


class BlogAdmin(admin.ModelAdmin):
	list_display = ("id" ,"name")
admin.site.register(BlogPost)


