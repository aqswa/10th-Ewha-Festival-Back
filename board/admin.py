from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
	list_display = ['day', 'date']
	list_display_links = ['day']

@admin.register(Booth)
class BoothAdmin(admin.ModelAdmin):
	list_display = ['id', 'user', 'name', 'created_at', 'updated_at']
	list_display_links = ['id']

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
	list_display = ['id', 'post', 'menu', 'image', 'price', 'is_soldout', 'created_at', 'updated_at']
	list_display_links = ['id']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ['id', 'user', 'post', 'content', 'created_at', 'updated_at']
	list_display_links = ['id']