from django.contrib import admin
from mysite.models import Question, Several

class ChoiceInline(admin.TabularInline):
    model = Several
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None , {'fields': ['question_text']}),
        ('Date?', {'fields': ['published_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]
    list_display = ('published_date', 'question_text')
    list_filter = ['question_text', 'published_date']
    search_fields = ['question_text', 'published_date']

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Several)