from django.contrib import admin
from dict import models
# Register your models here.
admin.site.register(models.User, models.UserAdmin)
admin.site.register(models.CET4, models.CET4Admin)
admin.site.register(models.CET6, models.CET6Admin)
admin.site.register(models.Note, models.NoteAdmin)
