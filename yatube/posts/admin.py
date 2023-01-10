from django.contrib import admin

from .models import Group, Post

class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'

# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin
admin.site.register(Group)
admin.site.register(Post, PostAdmin)