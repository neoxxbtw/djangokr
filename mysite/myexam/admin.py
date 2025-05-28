from django.contrib import admin

from mysite.myexam.models import ivexam


@admin.register(ivexam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'exam_date', 'is_public')
    list_filter = ('is_public', 'created_at')
    search_fields = ('title', 'users__email')
    date_hierarchy = 'exam_date'
    filter_horizontal = ('users',)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if '@' in search_term:
            queryset |= self.model.objects.filter(users__email=search_term)
        return queryset, use_distinct