from django.contrib import admin
from django.contrib.admin.options import ModelAdmin, TabularInline

from apps.polls.models import (
    Question,
    Choice,
)


class ChoiseAdmin(TabularInline):
    model = Choice
    ...


@admin.register(Question)
class QuestionAdmin(ModelAdmin):
    inlines = (ChoiseAdmin,)
