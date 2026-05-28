from django.shortcuts import render
from .models import Module, QuestionAnswer

def index(request):
    """Главная страница с вопросами и ответами"""
    modules = Module.objects.filter(is_active=True).prefetch_related('questions')
    
    # Берем первый активный модуль или None
    first_module = modules.first()
    questions = first_module.questions.all() if first_module else []
    
    context = {
        'modules': modules,
        'current_module': first_module,
        'questions': questions,
    }
    return render(request, 'index.html', context)