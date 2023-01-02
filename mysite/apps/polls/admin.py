from django.contrib import admin

from apps.polls.models import Question

admin.site.register(Question)
