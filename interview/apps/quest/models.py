from django.db import models

from django.utils import timezone

class Interview(models.Model):
    id = models.AutoField(primary_key=True)
    interview_title = models.CharField('Название опроса', max_length=100)
    interview_description = models.TextField('Описание опроса', blank=True)
    interview_pub_date = models.DateTimeField('Дата начала опроса', editable=False, default=timezone.now)
    interview_end_date = models.DateTimeField('Дата окончания опроса', default=timezone.now)

    def __str__(self):
        return self.interview_title

    def now_active(self):
        return self.interview_pub_date >= timezone.now()

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question_text = models.CharField('Текст вопроса', max_length=300)
    ANSWER_TYPE_CHOICES = (
        (1, 'Ответ текстом'),
        (2, 'Выбор одного варианта ответа'),
        (3, 'Выбор нескольких вариантов ответов'),
    )
    answer_type = models.PositiveSmallIntegerField('Тип вопроса', default=1, choices=ANSWER_TYPE_CHOICES)
    interview = models.ForeignKey(Interview, editable=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class AnswerOption(models.Model):
    id = models.AutoField(primary_key=True)
    answer_text = models.CharField('Текст ответа', max_length=300)
    question = models.ForeignKey(Question, editable=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответов'

class Result(models.Model):
    interview = models.ForeignKey(Interview, editable=False, on_delete=models.CASCADE)
    user_id = models.PositiveIntegerField('ID пользователя', editable=False)
    interview_date = models.DateTimeField('Дата опроса', editable=False, default=timezone.now)

    class Meta:
        verbose_name = 'Результат опроса'
        verbose_name_plural = 'Результаты опросов'

class ResultAnswer(models.Model):
    result = models.ForeignKey(Result, editable=False, on_delete=models.CASCADE)
    question_number = models.ForeignKey(Question, editable=False, on_delete=models.CASCADE)
    answer = models.TextField('Ответ пользователя', editable=False)