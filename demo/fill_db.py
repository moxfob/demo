import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
django.setup()

from demo_app.models import Module, QuestionAnswer

QuestionAnswer.objects.all().delete()
Module.objects.all().delete()

print("База данных успешно очищена!")