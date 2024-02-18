from django.contrib import admin
from .models import User,Note

class NoteAdmin(admin.ModelAdmin):
    list_display=['title','content','user']
    
admin.site.register(User)
admin.site.register(Note,NoteAdmin)
# Register your models here.
