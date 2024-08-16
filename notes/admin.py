from django.contrib import admin
from . import models
# Register your models here.

class NotesAdmin(admin.ModelAdmin):
    #We don't want any additional configuration on this for now
    list_display = ('title', )


admin.site.register(models.Notes, NotesAdmin)