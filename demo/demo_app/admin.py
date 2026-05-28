from django.contrib import admin
from .models import Module, QuestionAnswer

class QuestionAnswerInline(admin.TabularInline):
    model = QuestionAnswer
    extra = 3
    fields = ['file', 'order']
    ordering = ['order']

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active', 'questions_count']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'description']
    inlines = [QuestionAnswerInline]
    
    def questions_count(self, obj):
        return obj.questions.count()
    questions_count.short_description = 'Количество файлов'

@admin.register(QuestionAnswer)
class QuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_module_title', 'get_file_name', 'order']
    list_filter = ['module']
    search_fields = ['file']
    list_editable = ['order']
    
    def get_module_title(self, obj):
        return obj.module.title
    get_module_title.short_description = 'Модуль'
    get_module_title.admin_order_field = 'module__title'
    
    def get_file_name(self, obj):
        return obj.file.name if obj.file else 'Нет файла'
    get_file_name.short_description = 'Файл'