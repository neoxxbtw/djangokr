from django.contrib import admin
@admin.register(ivexam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'exam_date', 'is_public')
    list_filter = ('is_public', 'exam_date')
    search_fields = ('title',)

admin.site.register(ivexam)