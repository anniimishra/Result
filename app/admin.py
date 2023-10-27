from django.contrib import admin
from .models import *

admin.site.register(studentid)
admin.site.register(Department)
admin.site.register(student)
admin.site.register(subject)

class SubjectMarkAdmin(admin.ModelAdmin):
    list_display=['std','subject','marks']
admin.site.register(subjectmarks,SubjectMarkAdmin)
# Register your models here.
