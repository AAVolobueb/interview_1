from django.contrib import admin

from .models import Interview, Question, AnswerOption, Result

admin.site.register(Interview)
admin.site.register(Question)
admin.site.register(AnswerOption)
admin.site.register(Result)