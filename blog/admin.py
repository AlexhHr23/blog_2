from django.contrib import admin

from blog.models import Post, PostImage

class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1  # Número de formularios de imágenes vacíos para mostrar

class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline]

admin.site.register(Post, PostAdmin)