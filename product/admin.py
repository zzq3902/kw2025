from django.contrib import admin
from .models import Product, Comment

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'pub_date']
    search_fields = ['title']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['content_list', 'content', 'author', 'create_date', 'modify_date']
    search_fields = ['author']


admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
