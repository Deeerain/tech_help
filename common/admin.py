from django.contrib import admin
from . import models


@admin.register(models.Work)
class WorkAdmin(admin.ModelAdmin):
    pass
