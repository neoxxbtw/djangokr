from django.contrib import admin

from .models import ivexam


@admin.register(ivexam)
class ivexamAdmin(admin.ModelAdmin):

    search_fields = ('title', 'users__email')

    date_hierarchy = 'exam_date'

    filter_horizontal = ('users',)

    list_filter = ('is_public', 'created_at')

    list_display = ('title', 'created_at', 'exam_date', 'is_public')
