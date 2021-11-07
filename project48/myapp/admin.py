from django.contrib import admin
from .models import Bot, Game

# Register your models here.

class BotAdmin(admin.ModelAdmin):
    list_display = ['bot_id', 'name']
    # search_fields = ['bot_id', 'name', 'level']

admin.site.register(Bot, BotAdmin)
admin.site.register(Game)