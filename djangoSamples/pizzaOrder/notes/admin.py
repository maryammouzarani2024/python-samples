from django.contrib import admin
from . import models
from guardian.admin import GuardedModelAdmin

class NoteAdmin(GuardedModelAdmin):
    list_display=('title',)


admin.site.register(models.Notes, NoteAdmin)