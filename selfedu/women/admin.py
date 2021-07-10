from django.contrib import admin
from .models import Women, Category

class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

# Register your models here.
admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)