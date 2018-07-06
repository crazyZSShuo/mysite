from django.contrib import admin

# Register your models here.
from .models import Category,Tag,Post


class PostAdmin(admin.ModelAdmin): #  定制Admin后台

	list_display = ['title','created_time','modified_time','category','author']

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post,PostAdmin)
