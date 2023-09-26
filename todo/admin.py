from django.contrib import admin
from .models import *


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass


@admin.register(TodoStatus)
class TodoStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(TodoTags)
class TodoTagsAdmin(admin.ModelAdmin):
    pass
