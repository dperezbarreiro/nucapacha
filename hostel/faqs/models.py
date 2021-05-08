from django.db import models


class Faq(models.Model):

    question = models.CharField(max_length=255)
    answer = models.TextField()

    question_es = models.CharField(max_length=255, verbose_name='Pregunta')
    answer_es = models.TextField(verbose_name='Respuesta')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'