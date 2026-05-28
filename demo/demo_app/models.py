from django.db import models

class Module(models.Model):
    title = models.CharField('Название модуля', max_length=255)
    description = models.TextField('Описание', blank=True)
    order = models.IntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активен', default=True)
    
    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'
        ordering = ['order', 'id']
    
    def __str__(self):
        return self.title


class QuestionAnswer(models.Model):
    module = models.ForeignKey(
        Module, 
        on_delete=models.CASCADE, 
        related_name='questions',
        verbose_name='Модуль'
    )
    file = models.FileField('Файл', upload_to='uploads/', null=True, blank=True)
    order = models.IntegerField('Порядок', default=0)
    
    class Meta:
        verbose_name = 'Вопрос-ответ'
        verbose_name_plural = 'Вопросы-ответы'
        ordering = ['module', 'order', 'id']
    
    def __str__(self):
        return f"{self.module.title} - Файл {self.id}"