from django.contrib import admin
from django.http import HttpResponse
from .  import models

admin.site.register(models.Category)
admin.site.register(models.Course)


