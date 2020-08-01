from django.contrib import admin
from app.models import Post, Category
# Register your models here.


@admin.register(Category)
class Category_admin(admin.ModelAdmin):
    pass


@admin.register(Post)
class Post_admin(admin.ModelAdmin):
    pass


# @admin.register(PostCategories)
# class PostCategories_admin(admin.ModelAdmin):
#     pass
